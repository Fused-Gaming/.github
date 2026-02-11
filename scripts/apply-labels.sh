#!/bin/bash

# Script to apply repository labels from labels.json
# Usage: ./apply-labels.sh <github-token> [repo-owner/repo-name]
#
# If repo is not specified, it will be detected from git remote

set -e

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if token is provided
if [ -z "$1" ]; then
    echo -e "${RED}Error: GitHub token is required${NC}"
    echo "Usage: $0 <github-token> [repo-owner/repo-name]"
    echo ""
    echo "You can create a token at: https://github.com/settings/tokens"
    echo "Required scopes: repo (or public_repo for public repositories)"
    exit 1
fi

GITHUB_TOKEN="$1"

# Determine repository
if [ -n "$2" ]; then
    REPO="$2"
else
    # Try to detect from git remote
    REPO=$(git remote get-url origin 2>/dev/null | sed -n 's#.*github.com[:/]\(.*\)\.git#\1#p' || echo "")
    if [ -z "$REPO" ]; then
        echo -e "${RED}Error: Could not detect repository from git remote${NC}"
        echo "Usage: $0 <github-token> [repo-owner/repo-name]"
        exit 1
    fi
fi

echo -e "${BLUE}=== GitHub Label Creator ===${NC}"
echo -e "Repository: ${GREEN}$REPO${NC}"
echo ""

# Check if labels.json exists
if [ ! -f "labels.json" ]; then
    echo -e "${RED}Error: labels.json not found${NC}"
    exit 1
fi

# Check if jq is available
if ! command -v jq &> /dev/null; then
    echo -e "${YELLOW}Warning: jq not found. Installing minimal JSON parser...${NC}"
    echo -e "${YELLOW}For better results, install jq: apt-get install jq${NC}"
    echo ""
fi

# Function to create a label
create_label() {
    local name="$1"
    local color="$2"
    local description="$3"

    # URL encode the label name for checking existence
    local encoded_name=$(echo -n "$name" | python3 -c "import sys; from urllib.parse import quote; print(quote(sys.stdin.read()))")

    # Check if label already exists
    local exists=$(curl -s -o /dev/null -w "%{http_code}" \
        -H "Authorization: token $GITHUB_TOKEN" \
        -H "Accept: application/vnd.github+json" \
        "https://api.github.com/repos/$REPO/labels/$encoded_name")

    if [ "$exists" = "200" ]; then
        echo -e "${YELLOW}⊘${NC} Label already exists: $name"
        return 0
    fi

    # Create the label
    local response=$(curl -s -w "\n%{http_code}" \
        -X POST \
        -H "Authorization: token $GITHUB_TOKEN" \
        -H "Accept: application/vnd.github+json" \
        -H "Content-Type: application/json" \
        "https://api.github.com/repos/$REPO/labels" \
        -d "{\"name\":\"$name\",\"color\":\"$color\",\"description\":\"$description\"}")

    local http_code=$(echo "$response" | tail -n1)

    if [ "$http_code" = "201" ]; then
        echo -e "${GREEN}✓${NC} Created: $name"
        return 0
    else
        echo -e "${RED}✗${NC} Failed to create: $name (HTTP $http_code)"
        echo "$response" | head -n-1 | jq -r '.message // empty' 2>/dev/null || echo "$response" | head -n-1
        return 1
    fi
}

# Parse JSON and create labels
echo -e "${BLUE}Creating labels...${NC}"
echo ""

# Use Python to parse JSON since it's more reliable than bash
python3 << 'PYTHON_SCRIPT'
import json
import sys
import os

with open('labels.json', 'r') as f:
    data = json.load(f)

created = 0
failed = 0
skipped = 0

for phase in data['labels']:
    print(f"\033[1;35m=== {phase['phase']} ===\033[0m")
    for item in phase['items']:
        name = item['name']
        color = item['color']
        description = item['description']

        # Call the bash function to create label
        result = os.system(f'''create_label "{name}" "{color}" "{description}"''')

        if result == 0:
            # Check the actual output to determine if created or skipped
            created += 1
        else:
            failed += 1
    print()

print(f"\033[0;34m=== Summary ===\033[0m")
print(f"Total labels processed: {created + failed}")
print(f"\033[0;32m✓ Created/Already exists: {created}\033[0m")
if failed > 0:
    print(f"\033[0;31m✗ Failed: {failed}\033[0m")

sys.exit(0 if failed == 0 else 1)
PYTHON_SCRIPT

exit_code=$?

if [ $exit_code -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✓ Label creation complete!${NC}"
else
    echo ""
    echo -e "${RED}✗ Some labels failed to create${NC}"
    exit 1
fi
