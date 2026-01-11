#!/bin/bash

# Script to apply repository labels using GitHub CLI (gh)
# Usage: ./apply-labels-gh.sh [repo-owner/repo-name]
#
# Requires: gh CLI (https://cli.github.com/)
# Make sure you're authenticated: gh auth login

set -e

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[1;35m'
NC='\033[0m' # No Color

# Check if gh is installed
if ! command -v gh &> /dev/null; then
    echo -e "${RED}Error: GitHub CLI (gh) is not installed${NC}"
    echo "Install it from: https://cli.github.com/"
    echo ""
    echo "Alternatively, use apply-labels.sh with a GitHub token"
    exit 1
fi

# Check if authenticated
if ! gh auth status &>/dev/null; then
    echo -e "${RED}Error: Not authenticated with GitHub CLI${NC}"
    echo "Run: gh auth login"
    exit 1
fi

# Determine repository
if [ -n "$1" ]; then
    REPO="$1"
else
    # Use current repository
    REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner 2>/dev/null || echo "")
    if [ -z "$REPO" ]; then
        echo -e "${RED}Error: Could not detect repository${NC}"
        echo "Usage: $0 [repo-owner/repo-name]"
        exit 1
    fi
fi

echo -e "${BLUE}=== GitHub Label Creator (gh CLI) ===${NC}"
echo -e "Repository: ${GREEN}$REPO${NC}"
echo ""

# Check if labels.json exists
if [ ! -f "labels.json" ]; then
    echo -e "${RED}Error: labels.json not found${NC}"
    exit 1
fi

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is required${NC}"
    exit 1
fi

echo -e "${BLUE}Creating labels...${NC}"
echo ""

# Parse and create labels
python3 << 'PYTHON_SCRIPT'
import json
import subprocess
import sys

def create_label(repo, name, color, description):
    """Create a label using gh CLI"""
    try:
        # Check if label exists
        result = subprocess.run(
            ['gh', 'label', 'list', '-R', repo, '--json', 'name'],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            existing_labels = json.loads(result.stdout)
            if any(label['name'] == name for label in existing_labels):
                print(f"\033[0;33m⊘\033[0m Label already exists: {name}")
                return True

        # Create label
        result = subprocess.run(
            ['gh', 'label', 'create', name,
             '-R', repo,
             '-c', color,
             '-d', description],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(f"\033[0;32m✓\033[0m Created: {name}")
            return True
        else:
            print(f"\033[0;31m✗\033[0m Failed to create: {name}")
            if result.stderr:
                print(f"  Error: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"\033[0;31m✗\033[0m Error creating {name}: {e}")
        return False

# Get repo from arguments
repo = sys.argv[1] if len(sys.argv) > 1 else None
if not repo:
    print("Error: Repository not provided")
    sys.exit(1)

with open('labels.json', 'r') as f:
    data = json.load(f)

created = 0
failed = 0

for phase in data['labels']:
    print(f"\n\033[1;35m=== {phase['phase']} ===\033[0m")
    for item in phase['items']:
        if create_label(repo, item['name'], item['color'], item['description']):
            created += 1
        else:
            failed += 1

print(f"\n\033[0;34m=== Summary ===\033[0m")
print(f"Total labels processed: {created + failed}")
print(f"\033[0;32m✓ Success: {created}\033[0m")
if failed > 0:
    print(f"\033[0;31m✗ Failed: {failed}\033[0m")

sys.exit(0 if failed == 0 else 1)
PYTHON_SCRIPT "$REPO"

exit_code=$?

if [ $exit_code -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✓ Label creation complete!${NC}"
else
    echo ""
    echo -e "${RED}✗ Some labels failed to create${NC}"
    exit 1
fi
