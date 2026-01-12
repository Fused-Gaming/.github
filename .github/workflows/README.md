# GitHub Workflows Documentation

This directory contains automated workflows that help maintain Fused Gaming's organizational standards, goal tracking, and project management across all repositories.

## Workflows Overview

### 🏷️ Label Management

#### `sync-labels.yml`
**Purpose**: Synchronizes standardized labels across all organization repositories

**Triggers**:
- Weekly on Mondays at 00:00 UTC (automatic)
- When labels.yml is modified (automatic)
- Manual trigger via workflow_dispatch

**What it does**:
- Reads label definitions from `labels.yml`
- Creates or updates labels in the repository
- Ensures consistency across all repos
- Generates sync report

**Configuration**: Edit `labels.yml` to modify organization-wide labels

---

#### `auto-label-issues.yml`
**Purpose**: Automatically labels issues and PRs based on content and file changes

**Triggers**:
- When issues are opened, edited, or reopened
- When PRs are opened, edited, reopened, or synchronized

**What it does**:
- Analyzes title and description for keywords
- Detects priority level (critical, high, medium, low)
- Identifies type (bug, feature, documentation, etc.)
- Determines area/component (discord, web, api, etc.)
- Assigns size estimates (XS, S, M, L, XL)
- For PRs: Labels based on files changed
- Adds appropriate status labels

**Labels applied**:
- Priority: `priority: critical/high/medium/low`
- Type: `type: bug/feature/documentation/etc.`
- Area: `area: discord/web/bot/api/etc.`
- Status: `status: needs-triage/blocked/etc.`
- Size: `size: XS/S/M/L/XL`
- Special: `good first issue` for newcomer-friendly items

---

### 📋 Project Board Management

#### `add-to-project.yml`
**Purpose**: Automatically adds issues and PRs to the organization project board

**Triggers**:
- When issues are opened, reopened, or labeled
- When PRs are opened, reopened, or labeled

**What it does**:
- Adds high-priority items to the [project board](https://github.com/orgs/Fused-Gaming/projects/10)
- Adds strategic items (goals, proposals, governance)
- Adds quarterly-labeled items (Q1, Q2, Q3, Q4)
- Posts welcome comment with resources
- Links to governance documentation

**Target Board**: [Fused Gaming Goals & Initiatives](https://github.com/orgs/Fused-Gaming/projects/10)

**Auto-added items**:
- Priority: critical or high
- Type: goal-proposal, project-proposal, governance
- Labels: 2026, quarter tags

---

### 🎯 Goal Tracking & Alignment

#### `goal-alignment-check.yml`
**Purpose**: Ensures issues and PRs align with organizational strategic goals

**Triggers**:
- When issues are opened, edited, or labeled
- When PRs are opened, edited, labeled, or synchronized
- Daily at 9:00 UTC (automatic scan)
- Manual trigger via workflow_dispatch

**What it does**:
- Fetches current goals from GOALS.md
- Checks if strategic items mention relevant goals
- Comments on items to request goal alignment
- Confirms alignment when goals are mentioned
- Generates daily alignment reports
- Identifies goals without active work

**Benefits**:
- Maintains strategic focus
- Reduces scope creep
- Improves transparency
- Tracks goal progress

---

#### `quarterly-okr-tracker.yml`
**Purpose**: Tracks quarterly OKR progress and generates reports

**Triggers**:
- Monthly on the 1st at 10:00 UTC (automatic)
- Manual trigger with option to create review issue

**What it does**:
- Determines current quarter automatically
- Fetches all quarter-labeled issues/PRs
- Calculates completion rates overall and by type
- Generates monthly progress reports
- Creates quarterly review issues (end of quarter)
- Identifies at-risk OKRs (blocked or stale)
- Provides recommendations based on progress

**Reports include**:
- Total items vs completed
- Completion rate by type
- At-risk items (blocked or stale >14 days)
- Recommendations for improvement

**Quarterly reviews**: Automatically creates review issues in March, June, September, December

---

### 🎮 Existing Workflows

#### `play_tictactoe.yml`
**Purpose**: Interactive tic-tac-toe game on the organization profile

**Note**: This is an existing workflow and should be preserved.

---

## Configuration Files

### `labels.yml`
Defines all organization-wide labels with:
- **Priority labels**: critical, high, medium, low
- **Type labels**: bug, feature, documentation, security, etc.
- **Status labels**: needs-triage, blocked, in-review, approved
- **Size labels**: XS, S, M, L, XL (t-shirt sizing)
- **Area labels**: discord, web, bot, api, database, ui, backend
- **Quarter labels**: Q1, Q2, Q3, Q4
- **Special labels**: good first issue, help wanted, breaking change

**To modify**: Edit `labels.yml` and sync will run automatically

---

## Permissions Required

These workflows require the following permissions:
- `issues: write` - Create comments, add labels
- `pull-requests: write` - Label and manage PRs
- `contents: read` - Read repository files
- `repository-projects: write` - Add items to project boards

All workflows use `GITHUB_TOKEN` which is automatically provided by GitHub Actions.

---

## Manual Triggers

Some workflows can be manually triggered:

1. Go to **Actions** tab in repository
2. Select the workflow
3. Click **Run workflow**
4. Choose branch and options (if applicable)
5. Click **Run workflow** button

---

## Monitoring & Debugging

### View Workflow Runs
- Navigate to **Actions** tab
- Click on a workflow to see run history
- Click on a specific run to see logs

### Workflow Summaries
Most workflows generate summaries with:
- Actions taken
- Items processed
- Results and recommendations
- Links to relevant resources

### Troubleshooting

**Workflow not running?**
- Check trigger conditions are met
- Verify required labels exist
- Check workflow permissions
- Review error logs in Actions tab

**Labels not syncing?**
- Verify `labels.yml` syntax is correct
- Check workflow run logs
- Ensure GITHUB_TOKEN has permissions

**Items not added to board?**
- Verify project URL is correct
- Check if item has required labels
- Ensure GITHUB_TOKEN has project permissions

---

## Best Practices

### For Contributors
- Use descriptive titles with keywords
- Fill out issue/PR templates completely
- Add relevant labels manually if needed
- Reference goals in strategic items
- Link related issues and PRs

### For Maintainers
- Review auto-labeled items weekly
- Triage items in "needs-triage" status
- Update GOALS.md regularly
- Monitor quarterly OKR progress
- Respond to alignment check comments

### For Core Team
- Review monthly OKR reports
- Address at-risk items promptly
- Complete quarterly reviews on time
- Update label definitions as needed
- Adjust workflows based on learnings

---

## Workflow Interactions

```
Issue/PR Created
       ↓
auto-label-issues.yml
       ↓
add-to-project.yml
       ↓
goal-alignment-check.yml
       ↓
Project Board
       ↓
quarterly-okr-tracker.yml
       ↓
Reports & Reviews
```

---

## Maintenance

### Regular Tasks
- **Weekly**: Review auto-labeled items
- **Monthly**: Check OKR progress reports
- **Quarterly**: Complete OKR reviews
- **Annually**: Update goal tracking for new year

### Workflow Updates
When updating workflows:
1. Test changes in a fork or draft PR first
2. Document changes in this README
3. Announce major changes to team
4. Monitor first few runs after deployment

---

## Resources

- [GOVERNANCE.md](../GOVERNANCE.md) - Decision-making framework
- [GOALS.md](../GOALS.md) - Current strategic goals
- [PROJECT_BOARD_GUIDE.md](../PROJECT_BOARD_GUIDE.md) - Board usage guide
- [CONTRIBUTING.md](../CONTRIBUTING.md) - Contribution guidelines
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

---

## Support

Questions about workflows?
- **GitHub Discussions**: Org-wide questions
- **Issue**: Workflow-specific problems
- **Telegram**: [@fusedgg](https://t.me/fusedgg)
- **Core Team**: Tag @core-team in issues

---

**Last Updated**: January 2026
**Maintained by**: Fused Gaming Core Team
**Version**: 1.0

For workflow proposals or improvements, use the [Governance Proposal](https://github.com/Fused-Gaming/.github/issues/new?template=governance-proposal.yml) template.
