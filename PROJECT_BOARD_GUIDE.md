# GitHub Project Board Guide

## Overview

This guide explains how Fused Gaming uses GitHub Projects to track goals, initiatives, and work items in alignment with our governance framework.

**Active Project Boards**:
- [V.I.S.E. VLN-Certifications](https://github.com/orgs/Fused-Gaming/projects/5) - Currently active
- Fused Gaming Goals & Initiatives - Planned (see [ORG_AUDIT_RECOMMENDATIONS.md](ORG_AUDIT_RECOMMENDATIONS.md) Section 4.1)

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

### Automatic Behaviors
- New issues → Added to board (Backlog)
- Issue labeled `priority: critical` → Moved to Planned
- PR opened → Linked items move to Review
- PR merged → Linked items move to Done
- Issue closed → Moved to Done

### Manual Workflows
- Triage (weekly)
- Sprint planning (as needed)
- Quarterly review
- Annual planning

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
- [GOVERNANCE.md](GOVERNANCE.md) - Decision-making process
- [GOALS.md](GOALS.md) - Current strategic goals

### Templates
- [Issue Templates](.github/ISSUE_TEMPLATE/)
- [PR Template](.github/PULL_REQUEST_TEMPLATE.md)

### Support
- **GitHub Discussions**: Ask questions
- **Core Team**: Tag @core-team in issues
- **Telegram**: [@fusedgg](https://t.me/fusedgg)

---

## Document Classification

This document is classified **PUBLIC** per [DOCUMENT_CLASSIFICATION_POLICY.md](DOCUMENT_CLASSIFICATION_POLICY.md).

**Update triggers**: This document MUST be updated when:
- Project board structure changes (columns, views, fields)
- Label definitions are modified (`labels.yml`)
- Workflow automation affecting the board is changed
- New project boards are created or retired

---

## Continuous Improvement

This project board system is iterative:

- **Monthly**: Review automation and workflows
- **Quarterly**: Assess view configurations and labels
- **Annually**: Major process improvements

**Suggest improvements** via Governance Proposal issue!

---

**Last Updated**: February 6, 2026
**Next Review**: May 2026

Questions? Open a discussion or ask in our [Telegram channel](https://t.me/fusedgg)!
