# Cross-Repository Roadmap Automation
## Automatic Roadmap Updates from All Organization Repositories

**Created**: February 6, 2026
**Status**: Implementation Plan
**Classification**: INTERNAL - Technical Documentation

---

## Requirement

**Goal**: Automatically update `ROADMAP.md` whenever there's a commit to ANY repository in the Fused-Gaming organization, ensuring progress tracking, project boards, issues, and milestones stay synchronized.

**Scope**: All 35+ repositories in the Fused-Gaming organization

---

## Solution Architecture

### Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    Fused-Gaming Organization                     │
│                      (35+ Repositories)                          │
└────────────┬────────────────────────────────────┬────────────────┘
             │                                    │
             │ Commit/Issue/Milestone Events      │
             ▼                                    ▼
    ┌────────────────────┐            ┌─────────────────────┐
    │  Repository Hook   │            │  Organization Hook  │
    │  (per-repo event)  │            │  (org-wide events)  │
    └────────┬───────────┘            └──────────┬──────────┘
             │                                    │
             └──────────────────┬─────────────────┘
                                ▼
                    ┌───────────────────────┐
                    │  Central Aggregator   │
                    │  (.github/workflows)  │
                    └───────────┬───────────┘
                                │
                    ┌───────────┴───────────┐
                    │                       │
                    ▼                       ▼
          ┌─────────────────┐    ┌──────────────────┐
          │  GitHub API      │    │  Project Boards  │
          │  Data Fetcher    │    │  API             │
          └─────────┬────────┘    └────────┬─────────┘
                    │                      │
                    └──────────┬───────────┘
                               ▼
                   ┌────────────────────────┐
                   │  Roadmap Generator     │
                   │  (updates ROADMAP.md)  │
                   └────────────┬───────────┘
                                │
                                ▼
                   ┌────────────────────────┐
                   │  Commit & Push         │
                   │  Updated ROADMAP.md    │
                   └────────────────────────┘
```

---

## Implementation Strategy

### Option 1: GitHub Organization Webhooks (Recommended)

**Approach**: Use organization-level webhooks to listen to all repository events

**Pros**:
- ✅ Centralized event handling
- ✅ Covers all current and future repos automatically
- ✅ Single workflow to maintain
- ✅ Real-time updates

**Cons**:
- ⚠️ Requires organization admin access
- ⚠️ More complex setup
- ⚠️ Higher API usage

**Implementation**:

1. **Set up organization webhook** pointing to `.github` repository workflow
2. **Workflow triggers** on push, issues, milestones across all repos
3. **Aggregates data** via GitHub API
4. **Updates ROADMAP.md** automatically
5. **Commits changes** back to `.github` repo

---

### Option 2: Repository Dispatch Events

**Approach**: Each repository dispatches events to the `.github` repo

**Pros**:
- ✅ Works with free tier
- ✅ Explicit control per repo
- ✅ Easier debugging

**Cons**:
- ❌ Requires workflow in each repo
- ❌ Maintenance overhead for 35+ repos
- ❌ Manual setup for new repos

**Implementation**:

1. **Add workflow to each repo** that dispatches events
2. **`.github` repo listens** for repository_dispatch events
3. **Aggregates and updates** ROADMAP.md

---

### Option 3: Scheduled Sync (Simplest)

**Approach**: Run a scheduled workflow that polls all repositories

**Pros**:
- ✅ Simplest to implement
- ✅ No webhooks or dispatch needed
- ✅ Works with free tier
- ✅ Easy to debug

**Cons**:
- ❌ Not real-time (delay based on schedule)
- ❌ Higher API usage if frequent
- ❌ May hit rate limits

**Implementation**:

1. **Scheduled workflow** (e.g., hourly or daily)
2. **Queries GitHub API** for all repos
3. **Aggregates commits, issues, milestones**
4. **Updates ROADMAP.md** with latest data

---

## Recommended Solution: Hybrid Approach

**Combination of Option 1 (real-time) and Option 3 (scheduled fallback)**

### Primary: Organization Webhook (Real-time)
- Triggers on high-priority events (pushes to main, milestone changes)
- Updates ROADMAP.md within minutes

### Fallback: Scheduled Sync (Safety net)
- Runs daily to catch any missed events
- Ensures data consistency
- Full reconciliation of all data

---

## Workflow Implementation

### Workflow 1: Real-Time Roadmap Update

**File**: `.github/workflows/roadmap-update-realtime.yml`

```yaml
name: Roadmap Update (Real-time)

on:
  # Organization-wide events (requires org webhook configuration)
  repository_dispatch:
    types: [roadmap-update]

  # Manual trigger for testing
  workflow_dispatch:
    inputs:
      repository:
        description: 'Repository that triggered update'
        required: false
        type: string

  # Listen to events in this repo
  push:
    branches: [main, master]
    paths-ignore:
      - 'docs/planning/ROADMAP.md'
      - 'ROADMAP.md'

  issues:
    types: [opened, closed, reopened, labeled, unlabeled, milestoned, demilestoned]

  milestone:
    types: [created, closed, opened, edited, deleted]

permissions:
  contents: write
  issues: read
  pull-requests: read

jobs:
  update-roadmap:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install PyGithub python-dateutil pyyaml

      - name: Fetch organization data
        id: fetch-data
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          ORG_NAME: Fused-Gaming
        run: |
          python scripts/roadmap/fetch-org-data.py

      - name: Generate roadmap
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          ORG_NAME: Fused-Gaming
          TRIGGER_REPO: ${{ github.event.repository.name || inputs.repository || 'manual' }}
          TRIGGER_EVENT: ${{ github.event_name }}
        run: |
          python scripts/roadmap/generate-roadmap.py

      - name: Check for changes
        id: check-changes
        run: |
          if git diff --quiet docs/planning/ROADMAP.md; then
            echo "changed=false" >> $GITHUB_OUTPUT
          else
            echo "changed=true" >> $GITHUB_OUTPUT
          fi

      - name: Commit and push changes
        if: steps.check-changes.outputs.changed == 'true'
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add docs/planning/ROADMAP.md
          git commit -m "chore: auto-update roadmap from ${{ env.TRIGGER_REPO || 'scheduled sync' }}

          Updated roadmap with latest data from organization repositories.

          Trigger: ${{ github.event_name }}
          Repository: ${{ env.TRIGGER_REPO }}
          Timestamp: $(date -u +"%Y-%m-%d %H:%M:%S UTC")

          [skip ci]"
          git push

      - name: Summary
        if: steps.check-changes.outputs.changed == 'true'
        run: |
          echo "✅ Roadmap updated successfully" >> $GITHUB_STEP_SUMMARY
          echo "Triggered by: ${{ github.event_name }}" >> $GITHUB_STEP_SUMMARY
          echo "Repository: ${{ env.TRIGGER_REPO }}" >> $GITHUB_STEP_SUMMARY
```

---

### Workflow 2: Scheduled Full Sync

**File**: `.github/workflows/roadmap-sync-scheduled.yml`

```yaml
name: Roadmap Sync (Scheduled)

on:
  # Run daily at 00:00 UTC
  schedule:
    - cron: '0 0 * * *'

  # Manual trigger
  workflow_dispatch:

permissions:
  contents: write
  issues: read
  pull-requests: read

jobs:
  full-sync:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install PyGithub python-dateutil pyyaml tabulate

      - name: Full organization sync
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          ORG_NAME: Fused-Gaming
          SYNC_MODE: full
        run: |
          echo "🔄 Starting full organization sync..."
          python scripts/roadmap/fetch-org-data.py --full-sync
          python scripts/roadmap/generate-roadmap.py --full-sync

      - name: Check for changes
        id: check-changes
        run: |
          if git diff --quiet docs/planning/ROADMAP.md; then
            echo "changed=false" >> $GITHUB_OUTPUT
            echo "ℹ️ No changes detected" >> $GITHUB_STEP_SUMMARY
          else
            echo "changed=true" >> $GITHUB_OUTPUT
          fi

      - name: Commit and push changes
        if: steps.check-changes.outputs.changed == 'true'
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add docs/planning/ROADMAP.md
          git commit -m "chore: scheduled roadmap sync

          Full synchronization of roadmap with all organization repositories.

          Synced: $(date -u +"%Y-%m-%d %H:%M:%S UTC")
          Mode: Scheduled full sync

          [skip ci]"
          git push

      - name: Generate sync report
        if: steps.check-changes.outputs.changed == 'true'
        run: |
          echo "✅ Roadmap synchronized successfully" >> $GITHUB_STEP_SUMMARY
          echo "" >> $GITHUB_STEP_SUMMARY
          echo "### Changes Summary" >> $GITHUB_STEP_SUMMARY
          git diff --stat HEAD~1 HEAD docs/planning/ROADMAP.md >> $GITHUB_STEP_SUMMARY
```

---

## Python Scripts

### Script 1: Fetch Organization Data

**File**: `scripts/roadmap/fetch-org-data.py`

```python
#!/usr/bin/env python3
"""
Fetch data from all Fused-Gaming organization repositories.
Aggregates commits, issues, milestones, and project board data.
"""

import os
import json
import sys
from datetime import datetime, timedelta
from github import Github
from github.GithubException import GithubException

# Configuration
ORG_NAME = os.getenv('ORG_NAME', 'Fused-Gaming')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
OUTPUT_FILE = 'org-data.json'
FULL_SYNC = '--full-sync' in sys.argv

def fetch_org_data():
    """Fetch all relevant data from organization repositories."""

    if not GITHUB_TOKEN:
        print("❌ Error: GITHUB_TOKEN environment variable not set")
        sys.exit(1)

    g = Github(GITHUB_TOKEN)

    try:
        org = g.get_organization(ORG_NAME)
    except GithubException as e:
        print(f"❌ Error accessing organization: {e}")
        sys.exit(1)

    print(f"📊 Fetching data for {ORG_NAME}...")

    org_data = {
        'fetched_at': datetime.utcnow().isoformat(),
        'organization': ORG_NAME,
        'repositories': [],
        'summary': {
            'total_repos': 0,
            'active_repos': 0,
            'total_commits_30d': 0,
            'open_issues': 0,
            'open_milestones': 0,
            'total_contributors': set()
        }
    }

    # Time range for recent activity
    since_date = datetime.utcnow() - timedelta(days=30)

    repos = org.get_repos()

    for repo in repos:
        print(f"  📁 Processing {repo.name}...")

        try:
            # Skip archived repos unless full sync
            if repo.archived and not FULL_SYNC:
                continue

            repo_data = {
                'name': repo.name,
                'full_name': repo.full_name,
                'description': repo.description,
                'url': repo.html_url,
                'archived': repo.archived,
                'language': repo.language,
                'topics': repo.get_topics(),
                'stars': repo.stargazers_count,
                'forks': repo.forks_count,
                'open_issues': repo.open_issues_count,
                'updated_at': repo.updated_at.isoformat(),
                'recent_commits': [],
                'milestones': [],
                'issues': [],
                'contributors': []
            }

            # Fetch recent commits (last 30 days)
            try:
                commits = repo.get_commits(since=since_date)
                for commit in commits[:10]:  # Limit to 10 most recent
                    repo_data['recent_commits'].append({
                        'sha': commit.sha[:7],
                        'message': commit.commit.message.split('\n')[0],
                        'author': commit.commit.author.name,
                        'date': commit.commit.author.date.isoformat(),
                        'url': commit.html_url
                    })
                    org_data['summary']['total_commits_30d'] += 1
            except GithubException:
                pass  # Empty repo or no commits

            # Fetch milestones
            try:
                for milestone in repo.get_milestones(state='all'):
                    milestone_data = {
                        'title': milestone.title,
                        'state': milestone.state,
                        'description': milestone.description,
                        'due_on': milestone.due_on.isoformat() if milestone.due_on else None,
                        'progress': {
                            'open_issues': milestone.open_issues,
                            'closed_issues': milestone.closed_issues,
                            'total': milestone.open_issues + milestone.closed_issues,
                            'percent_complete': round(
                                (milestone.closed_issues / (milestone.open_issues + milestone.closed_issues) * 100)
                                if (milestone.open_issues + milestone.closed_issues) > 0 else 0,
                                1
                            )
                        },
                        'url': milestone.html_url
                    }
                    repo_data['milestones'].append(milestone_data)

                    if milestone.state == 'open':
                        org_data['summary']['open_milestones'] += 1
            except GithubException:
                pass

            # Fetch open issues (limit to 20 most recent)
            try:
                issues = repo.get_issues(state='open', sort='updated', direction='desc')
                for issue in issues[:20]:
                    if issue.pull_request:
                        continue  # Skip PRs

                    issue_data = {
                        'number': issue.number,
                        'title': issue.title,
                        'labels': [label.name for label in issue.labels],
                        'milestone': issue.milestone.title if issue.milestone else None,
                        'created_at': issue.created_at.isoformat(),
                        'updated_at': issue.updated_at.isoformat(),
                        'url': issue.html_url
                    }
                    repo_data['issues'].append(issue_data)
            except GithubException:
                pass

            # Fetch contributors
            try:
                contributors = repo.get_contributors()
                for contributor in contributors:
                    repo_data['contributors'].append({
                        'login': contributor.login,
                        'contributions': contributor.contributions
                    })
                    org_data['summary']['total_contributors'].add(contributor.login)
            except GithubException:
                pass

            org_data['repositories'].append(repo_data)
            org_data['summary']['total_repos'] += 1

            if len(repo_data['recent_commits']) > 0 or repo_data['open_issues'] > 0:
                org_data['summary']['active_repos'] += 1

            org_data['summary']['open_issues'] += repo_data['open_issues']

        except GithubException as e:
            print(f"    ⚠️  Error processing {repo.name}: {e}")
            continue

    # Convert set to count
    org_data['summary']['total_contributors'] = len(org_data['summary']['total_contributors'])

    # Save to file
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(org_data, f, indent=2)

    print(f"\n✅ Data fetched successfully!")
    print(f"   Total repositories: {org_data['summary']['total_repos']}")
    print(f"   Active repositories: {org_data['summary']['active_repos']}")
    print(f"   Open issues: {org_data['summary']['open_issues']}")
    print(f"   Open milestones: {org_data['summary']['open_milestones']}")
    print(f"   Recent commits (30d): {org_data['summary']['total_commits_30d']}")
    print(f"   Total contributors: {org_data['summary']['total_contributors']}")
    print(f"   Saved to: {OUTPUT_FILE}")

if __name__ == '__main__':
    fetch_org_data()
```

---

### Script 2: Generate Roadmap

**File**: `scripts/roadmap/generate-roadmap.py`

```python
#!/usr/bin/env python3
"""
Generate ROADMAP.md from aggregated organization data.
Creates a comprehensive roadmap with milestones, progress, and recent activity.
"""

import json
import os
import sys
from datetime import datetime
from collections import defaultdict

# Configuration
INPUT_FILE = 'org-data.json'
OUTPUT_FILE = 'docs/planning/ROADMAP.md'
ORG_NAME = os.getenv('ORG_NAME', 'Fused-Gaming')
TRIGGER_REPO = os.getenv('TRIGGER_REPO', 'unknown')
TRIGGER_EVENT = os.getenv('TRIGGER_EVENT', 'scheduled')

def load_org_data():
    """Load organization data from JSON file."""
    try:
        with open(INPUT_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: {INPUT_FILE} not found. Run fetch-org-data.py first.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing {INPUT_FILE}: {e}")
        sys.exit(1)

def generate_progress_bar(percent, width=20):
    """Generate a text-based progress bar."""
    filled = int(width * percent / 100)
    empty = width - filled
    return f"[{'█' * filled}{'░' * empty}] {percent}%"

def generate_roadmap(data):
    """Generate roadmap markdown content."""

    summary = data['summary']
    fetched_at = datetime.fromisoformat(data['fetched_at'])

    content = f"""# Fused Gaming - Organization Roadmap
## Project Progress & Activity Overview

**Last Updated**: {fetched_at.strftime('%B %d, %Y at %H:%M UTC')}
**Auto-generated from**: Organization-wide repository data
**Triggered by**: {TRIGGER_EVENT} ({TRIGGER_REPO})

---

## Quick Stats

| Metric | Value | Status |
|--------|-------|--------|
| **Total Repositories** | {summary['total_repos']} | {'🟢' if summary['total_repos'] > 30 else '🟡'} |
| **Active Repositories** | {summary['active_repos']} | {'🟢' if summary['active_repos'] > 10 else '🟡'} |
| **Open Issues** | {summary['open_issues']} | {'🟢' if summary['open_issues'] < 100 else '🟡' if summary['open_issues'] < 200 else '🔴'} |
| **Open Milestones** | {summary['open_milestones']} | {'🟢' if summary['open_milestones'] > 0 else '🔴'} |
| **Recent Commits (30d)** | {summary['total_commits_30d']} | {'🟢' if summary['total_commits_30d'] > 50 else '🟡' if summary['total_commits_30d'] > 20 else '🔴'} |
| **Total Contributors** | {summary['total_contributors']} | {'🟢' if summary['total_contributors'] > 10 else '🟡'} |

---

## Active Milestones Across Organization

"""

    # Aggregate all open milestones
    open_milestones = []
    for repo in data['repositories']:
        for milestone in repo['milestones']:
            if milestone['state'] == 'open':
                open_milestones.append({
                    'repo': repo['name'],
                    'repo_url': repo['url'],
                    **milestone
                })

    # Sort by progress (lowest first = most urgent)
    open_milestones.sort(key=lambda m: m['progress']['percent_complete'])

    if open_milestones:
        content += "| Milestone | Repository | Progress | Due Date |\n"
        content += "|-----------|------------|----------|----------|\n"

        for milestone in open_milestones:
            progress = milestone['progress']
            progress_bar = generate_progress_bar(progress['percent_complete'], width=15)
            due_date = milestone['due_on'].split('T')[0] if milestone['due_on'] else 'No due date'

            content += f"| [{milestone['title']}]({milestone['url']}) | "
            content += f"[{milestone['repo']}]({milestone['repo_url']}) | "
            content += f"{progress_bar}<br>{progress['closed_issues']}/{progress['total']} issues | "
            content += f"{due_date} |\n"
    else:
        content += "_No open milestones found across organization._\n"

    content += "\n---\n\n## Recent Activity (Last 30 Days)\n\n"

    # Aggregate recent commits by repository
    repos_with_activity = []
    for repo in data['repositories']:
        if repo['recent_commits']:
            repos_with_activity.append(repo)

    # Sort by most recent activity
    repos_with_activity.sort(key=lambda r: r['updated_at'], reverse=True)

    if repos_with_activity:
        for repo in repos_with_activity[:15]:  # Top 15 most active
            content += f"### [{repo['name']}]({repo['url']})\n\n"

            if repo['description']:
                content += f"_{repo['description']}_\n\n"

            content += f"**Language**: {repo['language'] or 'N/A'} | "
            content += f"**Stars**: {repo['stars']} | "
            content += f"**Open Issues**: {repo['open_issues']}\n\n"

            if repo['recent_commits']:
                content += "**Recent Commits**:\n"
                for commit in repo['recent_commits'][:5]:
                    commit_date = datetime.fromisoformat(commit['date']).strftime('%b %d')
                    content += f"- [`{commit['sha']}`]({commit['url']}) {commit['message']} - {commit['author']} ({commit_date})\n"
                content += "\n"

            if repo['milestones']:
                open_ms = [m for m in repo['milestones'] if m['state'] == 'open']
                if open_ms:
                    content += "**Active Milestones**:\n"
                    for ms in open_ms[:3]:
                        content += f"- [{ms['title']}]({ms['url']}) - {ms['progress']['percent_complete']}% complete\n"
                    content += "\n"

            content += "---\n\n"
    else:
        content += "_No recent activity found in the last 30 days._\n\n"

    content += "## Repository Categories\n\n"

    # Categorize repositories by topic/language
    categories = defaultdict(list)
    for repo in data['repositories']:
        if repo['archived']:
            categories['Archived'].append(repo)
        elif repo['language']:
            categories[repo['language']].append(repo)
        else:
            categories['Other'].append(repo)

    for category, repos in sorted(categories.items()):
        content += f"### {category} ({len(repos)} repositories)\n\n"
        for repo in repos:
            status = '🟢' if repo['open_issues'] == 0 else '🟡' if repo['open_issues'] < 10 else '🔴'
            content += f"- {status} [{repo['name']}]({repo['url']})"
            if repo['description']:
                content += f" - {repo['description']}"
            content += f" ({repo['open_issues']} open issues)\n"
        content += "\n"

    content += """---

## How This Roadmap is Updated

This roadmap is **automatically generated** from live data across all Fused Gaming repositories.

**Update Triggers**:
- ✅ Real-time: Commits to main/master branches
- ✅ Real-time: Issue state changes (opened, closed, labeled)
- ✅ Real-time: Milestone updates (created, edited, closed)
- ✅ Scheduled: Daily full sync at 00:00 UTC

**Data Sources**:
- GitHub API (commits, issues, milestones)
- Organization repositories (all 35+ repos)
- Project boards and tracking

**Accuracy**: This roadmap reflects the state of all repositories as of the last update timestamp shown at the top.

---

## Contributing to Projects

See individual repository README files for contribution guidelines.

**General Process**:
1. Review [CONTRIBUTING.md](../../CONTRIBUTING.md)
2. Check repository issues for "good first issue" labels
3. Join our [Telegram](https://t.me/fusedgg) for discussions
4. Submit PRs following our guidelines

---

## Related Documentation

- [Strategic Goals](GOALS.md) - Our 2026 strategic objectives
- [Milestones Overview](MILESTONES_OVERVIEW.md) - Detailed milestone tracking
- [Project Portfolio](../projects/PORTFOLIO.md) - Complete project descriptions
- [Governance](../governance/GOVERNANCE.md) - Decision-making framework

---

**🤖 Auto-generated** by `.github/workflows/roadmap-sync-scheduled.yml`
**📊 Data fetched** from {summary['total_repos']} repositories
**⏰ Next sync**: Scheduled daily at 00:00 UTC or on repository events

_Questions? Open an issue or join our [Telegram](https://t.me/fusedgg)_
"""

    return content

def main():
    """Main entry point."""
    print("📝 Generating roadmap...")

    data = load_org_data()
    roadmap_content = generate_roadmap(data)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    # Write to file
    with open(OUTPUT_FILE, 'w') as f:
        f.write(roadmap_content)

    print(f"✅ Roadmap generated successfully!")
    print(f"   Output: {OUTPUT_FILE}")
    print(f"   Repositories processed: {data['summary']['total_repos']}")

if __name__ == '__main__':
    main()
```

---

## Setup Instructions

### Step 1: Create Script Directory

```bash
mkdir -p scripts/roadmap
```

### Step 2: Add Scripts

1. Create `scripts/roadmap/fetch-org-data.py` with content above
2. Create `scripts/roadmap/generate-roadmap.py` with content above
3. Make scripts executable:
   ```bash
   chmod +x scripts/roadmap/*.py
   ```

### Step 3: Add Workflows

1. Create `.github/workflows/roadmap-update-realtime.yml`
2. Create `.github/workflows/roadmap-sync-scheduled.yml`

### Step 4: Install Dependencies

Add to `requirements.txt`:
```
PyGithub>=2.1.1
python-dateutil>=2.8.2
pyyaml>=6.0
tabulate>=0.9.0
```

### Step 5: Test Locally

```bash
# Export token
export GITHUB_TOKEN="your_token_here"
export ORG_NAME="Fused-Gaming"

# Test data fetch
python scripts/roadmap/fetch-org-data.py

# Test roadmap generation
python scripts/roadmap/generate-roadmap.py

# Check output
cat docs/planning/ROADMAP.md
```

---

## Configuration Options

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `GITHUB_TOKEN` | GitHub API token | - | ✅ Yes |
| `ORG_NAME` | Organization name | `Fused-Gaming` | ✅ Yes |
| `OUTPUT_FILE` | Roadmap output path | `docs/planning/ROADMAP.md` | ❌ No |
| `TRIGGER_REPO` | Repository that triggered update | `unknown` | ❌ No |
| `SYNC_MODE` | Sync mode (`full` or `incremental`) | `incremental` | ❌ No |

### Workflow Schedule

Adjust in `.github/workflows/roadmap-sync-scheduled.yml`:

```yaml
schedule:
  - cron: '0 */6 * * *'  # Every 6 hours
  # or
  - cron: '0 0 * * *'    # Daily at midnight
  # or
  - cron: '0 0 * * 1'    # Weekly on Monday
```

---

## Per-Repository Setup (Optional)

To trigger roadmap updates from individual repositories:

### Add to Each Repository

**File**: `.github/workflows/notify-roadmap-update.yml`

```yaml
name: Notify Roadmap Update

on:
  push:
    branches: [main, master]
  issues:
    types: [opened, closed, milestoned, demilestoned]
  milestone:
    types: [created, closed, opened, edited]

jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger roadmap update
        uses: peter-evans/repository-dispatch@v2
        with:
          token: ${{ secrets.ORG_ROADMAP_TOKEN }}
          repository: Fused-Gaming/.github
          event-type: roadmap-update
          client-payload: |
            {
              "repository": "${{ github.repository }}",
              "event": "${{ github.event_name }}",
              "ref": "${{ github.ref }}",
              "timestamp": "${{ github.event.head_commit.timestamp }}"
            }
```

**Note**: Requires `ORG_ROADMAP_TOKEN` secret with `repo` scope.

---

## Roadmap.md Features

### Auto-Generated Sections

1. **Quick Stats** - Organization-wide metrics
2. **Active Milestones** - All open milestones with progress bars
3. **Recent Activity** - Last 30 days of commits per repo
4. **Repository Categories** - Grouped by language/topic
5. **Update Information** - When and how updated

### Progress Tracking

- ✅ Visual progress bars for milestones
- ✅ Issue counts (open/closed)
- ✅ Recent commit history
- ✅ Contributor activity
- ✅ Repository health indicators

---

## Benefits

### ✅ Always Up-to-Date
- Real-time updates on significant events
- Daily scheduled sync as safety net
- No manual maintenance required

### ✅ Comprehensive View
- All 35+ repositories in one place
- Aggregated metrics and progress
- Easy to spot inactive projects

### ✅ Automated Tracking
- Commits tracked automatically
- Issues and milestones synchronized
- Project boards reflected in roadmap

### ✅ Transparency
- Community can see real progress
- Investors get accurate updates
- Contributors know where to help

---

## Maintenance

### Monthly Tasks
- [ ] Review roadmap accuracy
- [ ] Verify all repos are tracked
- [ ] Check for API rate limit issues
- [ ] Update script logic if needed

### Quarterly Tasks
- [ ] Update categorization logic
- [ ] Review which repos should be featured
- [ ] Optimize API calls for efficiency

---

## Troubleshooting

### Issue: Rate Limit Exceeded

**Solution**:
- Reduce sync frequency
- Use conditional requests (ETags)
- Cache API responses

### Issue: Roadmap Not Updating

**Check**:
1. Workflow run logs in Actions tab
2. Python script errors
3. GitHub token permissions
4. File permissions (write access)

### Issue: Missing Repositories

**Check**:
1. Repository visibility (public vs private)
2. Token permissions (org access)
3. Repository archived status
4. Script filtering logic

---

## Future Enhancements

### Phase 2
- [ ] Project board integration
- [ ] Pull request tracking
- [ ] Contributor leaderboard
- [ ] Burndown charts

### Phase 3
- [ ] Interactive dashboard (GitHub Pages)
- [ ] Email notifications on major changes
- [ ] Slack/Discord webhooks
- [ ] Custom metrics and KPIs

---

## Security Considerations

### Secrets Management
- ✅ Use GitHub secrets for tokens
- ✅ Never commit tokens to repository
- ✅ Rotate tokens quarterly
- ✅ Use minimal required permissions

### API Access
- ✅ Read-only access to most repos
- ✅ Write access only to `.github` repo
- ✅ Rate limit awareness
- ✅ Error handling for failed requests

---

## Success Metrics

### Adoption
- ✅ Roadmap updated within 5 minutes of commits
- ✅ 100% of repositories tracked
- ✅ Zero manual updates required
- ✅ < 1% update failures

### Quality
- ✅ Accurate progress tracking
- ✅ No stale data (< 24 hours old)
- ✅ All milestones synchronized
- ✅ Clear activity indicators

---

## Related Documentation

- [Documentation Structure Proposal](DOCS_STRUCTURE_PROPOSAL.md)
- [GitHub Actions Workflows](../.github/workflows/README.md)
- [API Integration Guide](../technical/API_DESIGN.md) *(to be created)*

---

**Status**: Implementation Ready
**Priority**: P1 (High)
**Complexity**: Medium
**Estimated Setup Time**: 4-6 hours

---

**Questions?** Open an issue with label `type: automation` or discuss in Telegram [@fusedgg](https://t.me/fusedgg)
