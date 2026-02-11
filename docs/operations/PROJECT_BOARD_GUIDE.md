# GitHub Project Board Guide

## Overview

This guide explains how Fused Gaming uses GitHub Projects to track goals, initiatives, and work items in alignment with our governance framework.

**Active Project Boards**:
- [V.I.S.E. VLN-Certifications](https://github.com/orgs/Fused-Gaming/projects/5) - Currently active
- [Fused Gaming Goals & Initiatives](https://github.com/orgs/Fused-Gaming/projects/10) - Primary strategic tracking board (see also [ORG_AUDIT_RECOMMENDATIONS.md](../audit/ORG_AUDIT_RECOMMENDATIONS.md) Section 4.1)

---

## Project #10 Setup & Configuration

### Status: ✅ Verified Setup Required

As of the latest verification (see Issue #21), **Project #10 "Fused Gaming Goals & Initiatives"** requires proper setup with the standardized column structure and automation rules documented below.

### Quick Setup Checklist

Use this checklist to set up or verify Project #10:

- [ ] **Create Project Board** (if not exists): Navigate to https://github.com/orgs/Fused-Gaming/projects and create new project
- [ ] **Set Project Name**: "Fused Gaming Goals & Initiatives"
- [ ] **Set Project Description**: "Strategic goals, quarterly OKRs, and organizational initiatives tracking"
- [ ] **Create 5 Columns** (in order, left to right):
  - [ ] 📋 Backlog
  - [ ] 🎯 Planned
  - [ ] 🚧 In Progress
  - [ ] 👀 Review
  - [ ] ✅ Done
- [ ] **Configure Automation Rules** (see detailed section below)
- [ ] **Test Workflow** (create test issue, verify automation)
- [ ] **Archive Test Items** (clean up after verification)
- [ ] **Update This Document** (mark setup as complete, add project URL)

### Detailed Column Configuration

Each column should be configured with specific automation rules:

#### 📋 Backlog
**Purpose**: Newly proposed items awaiting triage

**Automation Rules**:
- ✅ Auto-add: New issues with label `type: goal-proposal`
- ✅ Auto-add: New issues with label `type: project-proposal`
- ✅ Auto-add: New issues with label `status: needs-triage`
- ✅ Auto-add: All newly created issues (optional - can be disabled if too noisy)

**Manual Workflow**:
- Weekly triage review by core team
- Add priority and size labels during triage
- Move approved items to "Planned"

#### 🎯 Planned
**Purpose**: Approved work scheduled for current or upcoming quarter

**Automation Rules**:
- ✅ Auto-move: Issues labeled `priority: critical`
- ✅ Auto-move: Issues labeled `status: approved`
- ✅ Auto-move: Issues assigned to current milestone
- ✅ Auto-move: Issues labeled `quarter: current` (if using quarter labels)

**Manual Workflow**:
- Sprint planning: Select items to work on
- Assign target dates and milestones
- Ensure resources are allocated

#### 🚧 In Progress
**Purpose**: Work actively being done right now

**Automation Rules**:
- ✅ Auto-move: Issues assigned to a user (from Planned or Backlog)
- ✅ Auto-move: Issues labeled `status: in-progress`
- ✅ Auto-move: Issues with linked draft PR opened

**Manual Workflow**:
- Developers self-assign and move to this column
- Regular progress updates via comments
- Move to Review when PR is ready

#### 👀 Review
**Purpose**: Code review, testing, or approval stage

**Automation Rules**:
- ✅ Auto-move: PR opened and marked "Ready for Review"
- ✅ Auto-move: Issues labeled `status: in-review`
- ✅ Auto-move: Issues with linked PR requesting review

**Manual Workflow**:
- Reviewers provide feedback
- Authors address review comments
- Approved PRs ready for merge

**View Settings**:
- Sort by: Oldest first (items waiting longest get priority)
- Highlight: Items with no reviews after 48 hours

#### ✅ Done
**Purpose**: Completed and shipped work

**Automation Rules**:
- ✅ Auto-move: Linked PR merged to default branch
- ✅ Auto-move: Issue closed with label `resolution: completed`
- ✅ Auto-move: Issue closed (without `resolution: wontfix` or `resolution: duplicate`)
- ✅ Auto-archive: Items in Done for 30+ days (keeps board clean)

**Manual Workflow**:
- Verify deployment/completion
- Update related documentation (GOALS.md, etc.)
- Celebrate wins! 🎉

### Setting Up Automation Rules

To configure automation in GitHub Projects:

1. **Navigate to Project Settings**:
   - Go to https://github.com/orgs/Fused-Gaming/projects/10
   - Click the "⋯" menu → "Settings"

2. **Enable Built-in Automations**:
   - Go to "Workflows" tab
   - Enable "Auto-add to project" workflows
   - Enable "Auto-move" workflows per column

3. **Configure Label-Based Rules**:
   ```
   When: Issue labeled "type: goal-proposal"
   Then: Add to project → Move to "📋 Backlog"

   When: Issue labeled "priority: critical"
   Then: Move to "🎯 Planned"

   When: Issue assigned
   Then: Move to "🚧 In Progress"

   When: Pull request opened
   Then: Move to "👀 Review"

   When: Pull request merged
   Then: Move to "✅ Done"

   When: Issue closed
   Then: Move to "✅ Done"
   ```

4. **Configure Auto-Archive**:
   - In "✅ Done" column settings
   - Enable "Auto-archive items"
   - Set threshold: 30 days

### Testing Your Setup

After configuration, test the automation:

1. **Create Test Issue**:
   ```
   Title: [TEST] Verify Project Board Automation
   Labels: type: goal-proposal, status: needs-triage
   ```

2. **Verify Auto-Add**: Issue should appear in "📋 Backlog"

3. **Test Label Triggers**:
   - Add `priority: critical` → Should move to "🎯 Planned"
   - Assign to yourself → Should move to "🚧 In Progress"

4. **Test PR Workflow**:
   - Create draft PR linked to issue
   - Mark PR ready for review → Issue moves to "👀 Review"
   - Merge PR → Issue moves to "✅ Done"

5. **Clean Up**: Close and archive test issue

---

## Board Structure

### Columns/Status Fields

Our project boards use the following status columns:

1. **📋 Backlog**
   - Proposed items awaiting triage
   - Ideas under consideration
   - Low priority items for future

2. **🎯 Planned**
   - Approved and scheduled
   - Assigned to specific quarter/milestone
   - Resources allocated

3. **🚧 In Progress**
   - Actively being worked on
   - Someone is assigned
   - Regular updates expected

4. **👀 Review**
   - Awaiting code review
   - Testing in progress
   - Pending approval

5. **✅ Done**
   - Completed items
   - Shipped to production
   - Goals achieved

---

## Labels and Categorization

### Priority Labels
- `priority: critical` - Must complete immediately
- `priority: high` - Should complete this quarter
- `priority: medium` - Complete when possible
- `priority: low` - Future consideration

### Type Labels
- `type: goal-proposal` - Strategic goal proposals
- `type: project-proposal` - New project proposals
- `type: feature` - Feature requests
- `type: bug` - Bug reports
- `type: governance` - Governance changes
- `type: documentation` - Documentation work
- `type: infrastructure` - Infrastructure/DevOps

### Status Labels
- `status: needs-triage` - Needs review by core team
- `status: blocked` - Blocked by dependencies
- `status: in-review` - Under review
- `status: approved` - Approved, ready to start

### Size Labels (T-Shirt Sizing)
- `size: XS` - < 1 day
- `size: S` - 1-3 days
- `size: M` - 1 week
- `size: L` - 2-4 weeks
- `size: XL` - 1+ months

---

## Creating Project Items

### From Issues
1. Create issue using appropriate template
2. Add relevant labels
3. Link to project board
4. Assign priority and size
5. Move to appropriate column

### From Discussions
1. Start discussion in GitHub Discussions
2. If approved, convert to issue
3. Add to project board
4. Follow issue workflow

### Direct Draft Items
1. Create draft item on board
2. Add title and description
3. Convert to issue when ready
4. Fill out issue template details

---

## Tracking Goals and OKRs

### Strategic Goals (Annual)
- Each annual goal from GOALS.md has a tracking issue
- Issue title: `[GOAL 2026] Goal Name`
- Tracked in "Strategic Goals" view
- Updated quarterly with progress

### Quarterly OKRs
- Each OKR has its own issue or draft item
- Linked to parent strategic goal
- Key Results tracked as subtasks or linked issues
- Reviewed monthly in core team sync

### Project Milestones
- Use GitHub Milestones for major project phases
- Link related issues to milestone
- Track milestone progress
- Celebrate completion!

---

## Board Views

### Default View: All Items
Shows all items across all statuses

### View: This Quarter
- Filter: Current quarter items
- Useful for sprint planning
- Focus on short-term deliverables

### View: Strategic Goals
- Filter: `type: goal-proposal` + status approved
- High-level organizational view
- Quarterly review reference

### View: Needs Triage
- Filter: `status: needs-triage`
- Items awaiting core team review
- Reviewed weekly

### View: Blocked Items
- Filter: `status: blocked`
- Items needing attention
- Tracked for resolution

### View: By Priority
- Grouped by priority labels
- Helps focus on critical items
- Used in planning sessions

### View: By Team/Area
- Grouped by assignee or project
- Shows workload distribution
- Helps with capacity planning

---

## Workflow Examples

### Example 1: New Goal Proposal

1. **Community member** creates issue using "Goal Proposal" template
2. Issue automatically labeled `type: goal-proposal`, `status: needs-triage`
3. Issue added to project board in **Backlog**
4. **Core team** reviews weekly, adds priority label
5. If approved, moves to **Planned** with target quarter
6. When work begins, assign and move to **In Progress**
7. Update progress regularly
8. When complete, move to **Done** and close issue
9. Update GOALS.md with results

### Example 2: Quarterly OKR Tracking

1. **Core team** creates OKR issues at quarter start
2. Each KR is a separate issue or subtask
3. All linked to parent Objective issue
4. Tracked in "This Quarter" view
5. Monthly: Update progress on each KR
6. End of quarter: Mark complete, review results
7. Document learnings in GOALS.md

### Example 3: Bug to Fix

1. **User** reports bug via "Bug Report" template
2. Bug auto-added to board, labeled `type: bug`, `status: needs-triage`
3. **Maintainer** triages: assigns priority and size
4. If high priority, moves to **Planned** this sprint
5. **Developer** picks up, moves to **In Progress**, assigns self
6. Creates PR, moves to **Review**
7. After PR merge, moves to **Done** and closes

---

## Automation

**See [Project #10 Setup & Configuration](#project-10-setup--configuration) above for detailed automation rules and configuration steps.**

### Automatic Behaviors (Summary)

| Trigger | Action | Destination Column |
|---------|--------|-------------------|
| New issue with `type: goal-proposal` | Auto-add to project | 📋 Backlog |
| New issue with `type: project-proposal` | Auto-add to project | 📋 Backlog |
| Issue labeled `priority: critical` | Auto-move | 🎯 Planned |
| Issue labeled `status: approved` | Auto-move | 🎯 Planned |
| Issue assigned to user | Auto-move | 🚧 In Progress |
| Issue labeled `status: in-progress` | Auto-move | 🚧 In Progress |
| Pull request opened (linked issue) | Auto-move | 👀 Review |
| Issue labeled `status: in-review` | Auto-move | 👀 Review |
| Pull request merged | Auto-move | ✅ Done |
| Issue closed (completed) | Auto-move | ✅ Done |
| Item in Done for 30+ days | Auto-archive | (Archived) |

### Manual Workflows
- **Weekly**: Backlog triage and prioritization
- **Sprint Planning**: Move Planned items to In Progress
- **Daily/As-Needed**: Update item status, move cards manually when automation doesn't trigger
- **Monthly**: Progress review on strategic goals
- **Quarterly**: OKR review and planning
- **Annual**: Strategic goal setting and retrospective

### Manual Card Movement

While automation handles most transitions, you may need to manually move cards when:

1. **Reprioritizing Work**: Drag items between Backlog and Planned based on changing priorities
2. **Blocking Issues**: Move item back from In Progress to Planned if blocked
3. **Skipping Stages**: Move item directly to Done if completed without formal review (e.g., documentation fixes)
4. **Reverting Automation**: If automation moves an item incorrectly, drag it to the correct column
5. **Batch Operations**: During planning sessions, manually organize multiple items at once

**To manually move a card**:
- Simply drag and drop the card to the desired column
- Or click the "⋯" menu on the card → "Move to" → Select column

---

## Best Practices

### For Core Team
- **Triage regularly**: Review "Needs Triage" weekly
- **Keep board updated**: Move items as status changes
- **Add context**: Comment on blocked items
- **Update progress**: Monthly updates on goals
- **Link PRs**: Always link PRs to related issues

### For Contributors
- **Use templates**: Create issues with proper templates
- **Provide details**: Complete all required fields
- **Link issues**: Reference related issues and PRs
- **Update status**: Comment when status changes
- **Ask questions**: Use comments for clarification

### For Everyone
- **Search first**: Check for duplicates before creating
- **Be specific**: Clear titles and descriptions
- **Stay focused**: One issue per topic
- **Communicate**: Keep discussions respectful
- **Celebrate wins**: Acknowledge completed work

---

## Integration with Other Systems

### GitHub Discussions
- Strategic discussions happen here
- Successful discussions → Issues → Project board

### GitHub Actions
- Automated testing on PRs
- Automated deployment on merge
- Automated security scanning

### External Tools
- **Telegram**: [@fusedgg](https://t.me/fusedgg) - Quick updates and notifications
- **Twitter/X**: [@fuseddotgg](https://x.com/fuseddotgg) - Public announcements
- **LinkedIn**: [Fused Gaming](https://www.linkedin.com/company/fusedgg/) - Professional milestones

---

## Metrics and Reporting

### Tracked Metrics
- **Velocity**: Items completed per week/month
- **Cycle time**: Time from start to completion
- **Lead time**: Time from creation to completion
- **WIP limits**: Items in progress per person
- **Blocked time**: Time items spend blocked

### Monthly Reports
Generated from project board data:
- Items completed
- Goals progress
- Blockers resolved
- Upcoming priorities

### Quarterly Reviews
- OKR completion rate
- Strategic goal progress
- Process improvements
- Capacity planning

---

## Common Scenarios

### Scenario: Item is Blocked
1. Add label `status: blocked`
2. Comment explaining blocker
3. Move to "Blocked Items" view
4. Escalate if blocker persists >1 week
5. Remove label when unblocked

### Scenario: Changing Priorities
1. Core team discusses in sync or discussion
2. Update priority labels
3. Reorder backlog/planned items
4. Communicate changes to affected parties
5. Document decision rationale

### Scenario: Item Abandoned
1. Comment with context for abandonment
2. Close issue with explanation
3. Remove from board or move to archive
4. Update any linked items
5. Document learnings

### Scenario: Converting Discussion to Issue
1. Discussion reaches consensus
2. Create issue referencing discussion
3. Use appropriate template
4. Link back to discussion
5. Add to project board

---

## Resources

### Documentation
- [GitHub Projects Docs](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
- [GOVERNANCE.md](../governance/GOVERNANCE.md) - Decision-making process
- [GOALS.md](../planning/GOALS.md) - Current strategic goals

### Templates
- [Issue Templates](../../ISSUE_TEMPLATE/)
- [PR Template](../../PULL_REQUEST_TEMPLATE.md)

### Support
- **GitHub Discussions**: Ask questions
- **Core Team**: Tag @core-team in issues
- **Telegram**: [@fusedgg](https://t.me/fusedgg)

---

## Document Classification

This document is classified **PUBLIC** per [DOCUMENT_CLASSIFICATION_POLICY.md](../governance/DOCUMENT_CLASSIFICATION_POLICY.md).

**Update triggers**: This document MUST be updated when:
- Project board structure changes (columns, views, fields)
- Label definitions are modified (`labels.yml`)
- Workflow automation affecting the board is changed
- New project boards are created or retired

**Recent Updates**:
- **Feb 8, 2026**: Added comprehensive Project #10 setup documentation per Issue #21, including detailed automation rules, column configuration, and testing workflow

---

## Continuous Improvement

This project board system is iterative:

- **Monthly**: Review automation and workflows
- **Quarterly**: Assess view configurations and labels
- **Annually**: Major process improvements

**Suggest improvements** via Governance Proposal issue!

---

**Last Updated**: February 8, 2026
**Next Review**: May 2026
**Related Issues**: [#21 - Verify and Document Project Board Column Setup](https://github.com/Fused-Gaming/.github/issues/21)

Questions? Open a discussion or ask in our [Telegram channel](https://t.me/fusedgg)!
