# Label Governance Reference

**Version**: 2.0
**Last Updated**: February 6, 2026
**Next Review**: May 6, 2026
**Classification**: PUBLIC

This document is the authoritative reference for all labels across the Fused Gaming organization. It maps every label to its definition source, auto-labeling rules, and downstream workflow effects.

---

## Table of Contents

1. [Label Architecture](#1-label-architecture)
2. [Label Sources & Sync](#2-label-sources--sync)
3. [Complete Label Reference](#3-complete-label-reference)
4. [Auto-Labeling Rules](#4-auto-labeling-rules)
5. [Downstream Workflow Effects](#5-downstream-workflow-effects)
6. [Known Conflicts & Gaps](#6-known-conflicts--gaps)
7. [Maintenance & Application](#7-maintenance--application)

---

## 1. Label Architecture

### How Labels Flow

```
labels.yml (104 definitions)
       |
       v
sync-labels.yml ──> Creates/syncs labels across all org repos (weekly Monday 00:00 UTC)

Issue/PR Created or Edited
       |
       v
auto-label-issues.yml ──> Applies labels based on title/body keywords + PR file types
       |
       v
milestone-task-enforcement.yml ──> Auto-applies M*/T* labels, enforces on strategic items
       |
       v
add-to-milestone.yml ──> Strategic items → "Strategic Backlog" milestone + welcome comment
       |
       v
goal-alignment-check.yml ──> Strategic items → goal alignment check comment
       |
       v
quarterly-okr-tracker.yml ──> Quarter-labeled items → OKR progress reports
```

### Label Definition Sources

| Source | Count | Purpose | Used By |
|---|---|---|---|
| `.github/labels.yml` | 104 | **Primary** - org-wide label definitions | `sync-labels.yml` (weekly sync to all repos) |
| `labels.json` | 27 | **Legacy** - shell script application | `apply-labels.sh`, `apply-labels-gh.sh` |
| `auto-label-issues.yml` | 0 | All previously implicit labels now added to `labels.yml` | N/A |

> **Note**: All 27 labels in `labels.json` are duplicated in `labels.yml`. The `labels.json` file and its shell scripts are a legacy mechanism predating the `sync-labels.yml` workflow.

---

## 2. Label Sources & Sync

### Primary: `.github/labels.yml`

Synced to all org repos by `sync-labels.yml` every Monday at 00:00 UTC, when `labels.yml` is modified, or via manual trigger. Prune mode is **disabled** (repos keep extra labels).

### Legacy: `labels.json`

Applied via `apply-labels.sh` (GitHub API with token) or `apply-labels-gh.sh` (GitHub CLI). These scripts are manual, one-time application tools. All labels in `labels.json` are already included in `labels.yml`.

### ~~Implicit: Workflow-Created Labels~~ - RESOLVED

Previously, five `type:` labels were applied by workflows but not defined in `labels.yml`. These have now been added to `labels.yml` and will sync org-wide. See "Type Labels (Workflow-Applied)" in Section 3.

---

## 3. Complete Label Reference

### Priority Labels

| Label | Color | Auto-Applied | Trigger Keywords | Downstream Effects |
|---|---|---|---|---|
| `🚨Priority:CRITICAL` | `#ed0e6e` | Yes | Title: `[critical]`, `[urgent]`, `🚨`; Body: `priority: critical`, `p0` | Milestone: Strategic Backlog; Goal alignment check |
| `🔴Priority:HIGH` | `#76020c` | Yes | Title: `[high]`, `🔴`; Body: `priority: high`, `p1` | Milestone: Strategic Backlog; Goal alignment check; OKR at-risk if stale |
| `🟠Priority:MEDIUM` | `#d8bb2f` | Yes | Title: `[medium]`, `🟠`; Body: `priority: medium`, `p2` | None |
| `🟢Priority:LOW` | `#0e8a16` | **No** | Manual only | None |
| `ℹ️Priority:INFO` | `#3e0aae` | Yes | Title: `[low]`, `ℹ️`; Body: `priority: low`, `p4` | None |

### Project Labels

| Label | Color | Auto-Applied | Trigger Keywords | Downstream Effects |
|---|---|---|---|---|
| `☕DRIFT` | `#6f4e37` | Yes | Title/body: `drift` | None |
| `💎GAMBAREWARDS` | `#b9f2ff` | Yes | Title/body: `gambarewards` | None |
| `🔫GAMBARELOAD` | `#ff6b6b` | Yes | Title/body: `gambareload` | None |
| `🔬VLN` | `#00d2ff` | Yes | Title/body: `vln` | None |
| `🏆LEADERBOARDS` | `#ffd700` | Yes | Title/body: `leaderboard` | None |

### Team / Role Labels

| Label | Color | Auto-Applied | Trigger Keywords | Downstream Effects |
|---|---|---|---|---|
| `👷DEV` | `#1f77b4` | No | Manual only | None |
| `💉DEVOPS` | `#ff7f0e` | Yes | Body: `devops`, `ci/cd`, `deployment` | None |
| `🎨DESIGN` | `#e377c2` | Yes | Body: `design`, `ui/ux` | None |
| `🌐DOMAIN` | `#8c564b` | No | Manual only | None |
| `⚖️LEGAL` | `#7f7f7f` | No | Manual only | None |
| `💰STAKE-HOLDERS` | `#bcbd22` | No | Manual only | None |

### Status Labels

| Label | Color | Auto-Applied | Trigger Keywords | Downstream Effects |
|---|---|---|---|---|
| `✅COMPLETED` | `#0e8a16` | No | Manual only | None |
| `🗺️PLANNED` | `#c5def5` | Yes | Body: `planned`; Title: `planned`, `🗺️` | None |
| `🐌BLOCKED` | `#b60205` | Yes | Body: `blocked`; Title: `[blocked]`, `🐌` | None |
| `🎯IN-PROGRESS` | `#c2e0c6` | No | Manual only | None |
| `⏳WAITING` | `#fef2c0` | No | Manual only | None |
| `status: needs-triage` | `#ededed` | Yes | Unassigned issues (no assignee) | None |
| `status: in-review` | `#fbca04` | No | Manual only | None |
| `status: approved` | `#0e8a16` | No | Manual only | None |

### Governance Labels

| Label | Color | Auto-Applied | Trigger Keywords | Downstream Effects |
|---|---|---|---|---|
| `❎GOVERNANCE` | `#5319e7` | Yes | Title: `[governance]`, `❎`; Body: `type: governance`, `governance` | Milestone: Strategic Backlog; Goal alignment check |
| `🙋‍♂️VOTE = YEA` | `#0e8a16` | No | Manual only (voting) | None |
| `🙅‍♂️VOTE = NAY` | `#d73a4a` | No | Manual only (voting) | None |

### Type Labels (Proposals)

| Label | Color | Auto-Applied | Trigger Keywords | Downstream Effects |
|---|---|---|---|---|
| `type: goal-proposal` | `#7057ff` | Yes | Title: `[goal]`, `goal:`; Body: `type: goal-proposal` | Milestone: Strategic Backlog; Goal alignment check; Welcome comment |
| `type: project-proposal` | `#8b5cf6` | Yes | Title: `[project]`; Body: `type: project-proposal` | Milestone: Strategic Backlog; Goal alignment check; Welcome comment |

### Type Labels (PR File Detection - PRs Only)

These are applied by `auto-label-issues.yml` Step 2 based on changed files in PRs.

| Label | Color | Trigger (File Pattern) | Defined in `labels.yml`? |
|---|---|---|---|
| `type: documentation` | N/A | Files matching `.md` or `README` | **No** |
| `type: infrastructure` | N/A | Files matching `.yml`, `.yaml`, or `.github/workflows` | **No** |
| `type: test` | N/A | Files matching `test` or `spec` | **No** |
| `type: governance` | N/A | Files matching `GOVERNANCE` or `CONTRIBUTING` | **No** |
| `type: security` | N/A | Files matching `SECURITY` | **No** |

### Standard GitHub Labels

| Label | Color | Auto-Applied | Trigger Keywords | Downstream Effects |
|---|---|---|---|---|
| `bug` | `#d73a4a` | Yes | Title: `bug`, `fix`, `error`, `issue` | None |
| `documentation` | `#0075ca` | Yes | Title: `docs`, `documentation`, `readme` | None |
| `enhancement` | `#a2eeef` | Yes | Title: `enhance`, `improve`, `update` | None |
| `question` | `#d876e3` | Yes | Title: `question`, `help`, `how to` | None |
| `duplicate` | `#cfd3d7` | No | Manual only | None |
| `wontfix` | `#ffffff` | No | Manual only | None |
| `invalid` | `#e4e669` | No | Manual only | None |

### Size Labels (Estimation)

All auto-applied based on body content or body length.

| Label | Color | Auto-Applied | Trigger Rule |
|---|---|---|---|
| `size: XS` | `#c2e0c6` | Yes | Body contains `size: xs` **OR** body.length < 200 |
| `size: S` | `#bfdadc` | Yes | Body contains `size: s` **OR** body.length 200-499 |
| `size: M` | `#fef2c0` | Yes | Body contains `size: m` **OR** body.length 500-999 |
| `size: L` | `#fad8c7` | Yes | Body contains `size: l` **OR** body.length 1000-1999 |
| `size: XL` | `#f7c6c7` | Yes | Body contains `size: xl` **OR** body.length >= 2000 |

### Milestone Labels (Roadmap Tracking)

Maps to the organizational milestones defined in [MILESTONES_OVERVIEW.md](../planning/MILESTONES_OVERVIEW.md). Auto-applied by `milestone-task-enforcement.yml` when title/body contains milestone references.

| Label | Color | Auto-Applied | Trigger Keywords | Downstream Effects |
|---|---|---|---|---|
| `milestone: M0` | `#6f42c1` | Yes | `M0`, `milestone 0`, `investor readiness` | Enforcement comment if strategic but missing |
| `milestone: M1` | `#7c3aed` | Yes | `M1`, `milestone 1`, `project visibility`, `documentation milestone` | Enforcement comment if strategic but missing |
| `milestone: M2` | `#8b5cf6` | Yes | `M2`, `milestone 2`, `onboarding` | Enforcement comment if strategic but missing |
| `milestone: M3` | `#a78bfa` | Yes | `M3`, `milestone 3`, `community activation` | Enforcement comment if strategic but missing |
| `milestone: M4` | `#c4b5fd` | Yes | `M4`, `milestone 4`, `technical foundation` | Enforcement comment if strategic but missing |
| `milestone: M5` | `#ddd6fe` | Yes | `M5`, `milestone 5`, `community growth` | Enforcement comment if strategic but missing |
| `milestone: M6` | `#ede9fe` | Yes | `M6`, `milestone 6`, `product milestones` | Enforcement comment if strategic but missing |

### Task Sequence Labels

Track task order within milestones. Auto-applied by `milestone-task-enforcement.yml` when title/body contains task references (e.g., `T1`, `task 3`).

| Label | Color | Auto-Applied | Trigger Keywords |
|---|---|---|---|
| `task: T1` | `#0d419d` | Yes | `T1`, `task 1` |
| `task: T2` | `#1d5cbf` | Yes | `T2`, `task 2` |
| `task: T3` | `#2e77e0` | Yes | `T3`, `task 3` |
| `task: T4` | `#4f91f5` | Yes | `T4`, `task 4` |
| `task: T5` | `#6ba5f7` | Yes | `T5`, `task 5` |
| `task: T6` | `#89bbf9` | Yes | `T6`, `task 6` |
| `task: T7` | `#a6d0fb` | Yes | `T7`, `task 7` |
| `task: T8` | `#c3e0fd` | Yes | `T8`, `task 8` |
| `task: T9` | `#dfeffe` | Yes | `T9`, `task 9` |

### Type Labels (Workflow-Applied)

Previously missing from `labels.yml` (Conflict 2 resolved). Now synced org-wide.

| Label | Color | Auto-Applied | Trigger (Source) |
|---|---|---|---|
| `type: documentation` | `#0075ca` | Yes | PR files: `.md`, `README`; `doc-staleness-audit.yml` |
| `type: infrastructure` | `#006b75` | Yes | PR files: `.yml`, `.yaml`, `.github/workflows` |
| `type: test` | `#d4c5f9` | Yes | PR files: `test`, `spec` |
| `type: governance` | `#5319e7` | Yes | PR files: `GOVERNANCE`, `CONTRIBUTING`; `quarterly-okr-tracker.yml` |
| `type: security` | `#d93f0b` | Yes | PR files: `SECURITY` |

### Quarter / Year Labels

| Label | Color | Auto-Applied | Downstream Effects |
|---|---|---|---|
| `quarter: Q1` | `#c5def5` | No | Milestone: Strategic Backlog; OKR tracking |
| `quarter: Q2` | `#bfd4f2` | No | Milestone: Strategic Backlog; OKR tracking |
| `quarter: Q3` | `#d4c5f9` | No | Milestone: Strategic Backlog; OKR tracking |
| `quarter: Q4` | `#e99695` | No | Milestone: Strategic Backlog; OKR tracking |
| `2026` | `#0e8a16` | No | Milestone: Strategic Backlog; OKR tracking |
| `2027` | `#2ea44f` | No | None (future) |

### Area / Component Labels

| Label | Color | Auto-Applied | Trigger Keywords |
|---|---|---|---|
| `area: discord` | `#5865F2` | Yes | Title/body: `discord` |
| `area: web` | `#006b75` | Yes | Title/body: `web`, `website` |
| `area: bot` | `#1f6feb` | Yes | Title/body: `bot` |
| `area: api` | `#0969da` | Yes | Title/body: `api` |
| `area: database` | `#bf4b8a` | No | Manual only |

### Instruction Labels

| Label | Color | Auto-Applied | Downstream Effects |
|---|---|---|---|
| `✔️ALWAYS` | `#0e8a16` | No | None |
| `❌NEVER` | `#d73a4a` | No | None |

### Special / Utility Labels

| Label | Color | Auto-Applied | Trigger Keywords | Downstream Effects |
|---|---|---|---|---|
| `good first issue` | `#7057ff` | Yes | Title/body: `good first issue`; OR title contains (`simple`/`easy`) AND (`fix`/`update`) | None |
| `help wanted` | `#008672` | No | Manual only | None |
| `breaking change` | `#d73a4a` | No | Manual only | None |
| `dependencies` | `#0366d6` | No | Manual only | None |
| `🔧TOOLING` | `#fbca04` | No | Manual only | None |

### Transparency & Communication Labels (from `labels.json`)

| Label | Color | Auto-Applied | Downstream Effects |
|---|---|---|---|
| `📢ANNOUNCEMENT` | `#0e8a16` | No | None |
| `📝CHANGELOG` | `#1d76db` | No | None |
| `🎮PLAYER-IMPACT` | `#e99695` | No | None |
| `💥BREAKING-CHANGE` | `#b60205` | No | None |

### Deployment Labels (from `labels.json`)

| Label | Color | Auto-Applied | Downstream Effects |
|---|---|---|---|
| `🚀READY-FOR-DEPLOY` | `#0e8a16` | No | None |
| `✅PRODUCTION` | `#0e8a16` | No | None |
| `🔄STAGING` | `#fbca04` | No | None |

### Security & Trust Labels (from `labels.json`)

| Label | Color | Auto-Applied | Downstream Effects |
|---|---|---|---|
| `🔒SECURITY` | `#d93f0b` | No | None |
| `🛡️AUDIT` | `#5319e7` | No | None |
| `🔐COMPLIANCE` | `#b60205` | No | None |

### Quality & Workflow Labels (from `labels.json`)

| Label | Color | Auto-Applied | Downstream Effects |
|---|---|---|---|
| `🔍INVESTIGATING` | `#d4c5f9` | No | None |
| `✨FEATURE` | `#a2eeef` | No | None |
| `♻️REFACTOR` | `#c5def5` | No | None |
| `📈IMPROVEMENT` | `#84b6eb` | No | None |
| `💼BUSINESS-DECISION` | `#d4c5f9` | No | None |
| `📊REPORTING` | `#bfdadc` | No | None |
| `💡NEEDS-SPEC` | `#f9d0c4` | No | None |
| `🧪TESTING` | `#d4c5f9` | No | None |
| `✅VERIFIED` | `#0e8a16` | No | None |
| `🐛REGRESSION` | `#ee0701` | No | None |
| `👀NEEDS-REVIEW` | `#fbca04` | No | None |
| `🏷️RELEASE` | `#5319e7` | No | None |
| `💬DISCUSSION` | `#cc317c` | No | None |
| `🔥HOTFIX` | `#d93f0b` | No | None |

---

## 4. Auto-Labeling Rules

**Workflow**: `auto-label-issues.yml`
**Triggers**: Issues (opened, edited, reopened) and PRs (opened, edited, reopened, synchronized)

### Step 1: Title & Body Content Analysis

Rules are evaluated in priority order within each category. For Priority and Type, only the **first match** applies (else-if chain). For Project, Area, Team, Status, and Special, **all matches** apply (independent if statements).

#### Priority (first match wins)
```
[critical] OR [urgent] OR 🚨 in title, OR "priority: critical" OR "p0" in body → 🚨Priority:CRITICAL
[high] OR 🔴 in title, OR "priority: high" OR "p1" in body                   → 🔴Priority:HIGH
[low] OR ℹ️ in title, OR "priority: low" OR "p4" in body                     → ℹ️Priority:INFO
[medium] OR 🟠 in title, OR "priority: medium" OR "p2" in body               → 🟠Priority:MEDIUM
```

#### Type (first match wins)
```
[goal] OR "goal:" in title, OR "type: goal-proposal" in body → type: goal-proposal
[project] in title, OR "type: project-proposal" in body      → type: project-proposal
[governance] OR ❎ in title, OR "governance" in body          → ❎GOVERNANCE
"bug" OR "fix" OR "error" OR "issue" in title                 → bug
"docs" OR "documentation" OR "readme" in title                → documentation
"enhance" OR "improve" OR "update" in title                   → enhancement
"question" OR "help" OR "how to" in title                     → question
```

#### Project (all matches)
```
"drift" in title/body           → ☕DRIFT
"gambarewards" in title/body    → 💎GAMBAREWARDS
"gambareload" in title/body     → 🔫GAMBARELOAD
"vln" in title/body             → 🔬VLN
"leaderboard" in title/body     → 🏆LEADERBOARDS
```

#### Area (all matches)
```
"discord" in title/body         → area: discord
"web" OR "website" in title     → area: web
"bot" in title/body             → area: bot
"api" in title/body             → area: api
```

#### Team (all matches)
```
"devops" OR "ci/cd" OR "deployment" in body  → 💉DEVOPS
"design" OR "ui/ux" in body                  → 🎨DESIGN
```

#### Status
```
Issue has no assignee           → status: needs-triage
"blocked" in body OR title      → 🐌BLOCKED
"planned" in body OR title      → 🗺️PLANNED
```

#### Size (always applied, first match wins)
```
"size: xs" in body OR body < 200 chars   → size: XS
"size: s" in body OR body < 500 chars    → size: S
"size: m" in body OR body < 1000 chars   → size: M
"size: l" in body OR body < 2000 chars   → size: L
"size: xl" in body OR body >= 2000 chars → size: XL
```

#### Special
```
"good first issue" in title/body, OR ("simple"/"easy" AND "fix"/"update") in title → good first issue
```

### Step 2: PR File Detection (PRs Only)

| File Pattern | Label Applied |
|---|---|
| `.md` or `README` | `type: documentation` |
| `.yml`, `.yaml`, `.github/workflows` | `type: infrastructure` |
| `test` or `spec` | `type: test` |
| `GOVERNANCE` or `CONTRIBUTING` | `type: governance` |
| `SECURITY` | `type: security` |

---

## 5. Downstream Workflow Effects

### `add-to-milestone.yml` - Strategic Backlog Assignment

**Triggers**: Issues/PRs opened, reopened, or labeled

Labels that trigger milestone assignment (uses `.includes()` matching):

| Label Pattern | Effect |
|---|---|
| Any label containing `goal-proposal` | Assigned to "Strategic Backlog" milestone + welcome comment |
| Any label containing `project-proposal` | Assigned to "Strategic Backlog" milestone + welcome comment |
| Any label containing `GOVERNANCE` | Assigned to "Strategic Backlog" milestone + welcome comment |
| Any label containing `Priority:CRITICAL` | Assigned to "Strategic Backlog" milestone + welcome comment |
| Any label containing `Priority:HIGH` | Assigned to "Strategic Backlog" milestone + welcome comment |
| Any label containing `quarter:` | Assigned to "Strategic Backlog" milestone |
| Any label containing `2026` | Assigned to "Strategic Backlog" milestone |

### `goal-alignment-check.yml` - Strategic Alignment

**Triggers**: Issues/PRs opened, edited, labeled; Daily at 9:00 UTC

Labels that trigger alignment check (uses `.includes()` matching):

| Label Pattern | Effect |
|---|---|
| Any label containing `goal` | Checks if body/title references GOALS.md goals; comments if not aligned |
| Any label containing `project-proposal` | Same alignment check |
| Any label containing `governance` | Same alignment check |
| Any label containing `priority: critical` | Same alignment check |
| Any label containing `priority: high` | Same alignment check |

### `quarterly-okr-tracker.yml` - OKR Progress

**Triggers**: Monthly on 1st at 10:00 UTC

| Label | Role in OKR Tracking |
|---|---|
| `quarter: Q1/Q2/Q3/Q4` | Identifies items belonging to current quarter |
| `2026` | Combined with quarter label for OKR search |
| `type:*` labels | Categorizes items in progress report by type |
| `status: blocked` | Flags items as "at-risk" in monthly report |
| `priority: high` | Combined with stale detection (>14 days) for at-risk alerts |

### `milestone-task-enforcement.yml` - Milestone & Task Tracking

**Triggers**: Issues/PRs opened, edited, labeled; PRs to main/master

| Label Pattern | Effect |
|---|---|
| `milestone: M0` through `milestone: M6` | Auto-applied from title/body keywords; strategic items without milestone get enforcement comment |
| `task: T1` through `task: T9` | Auto-applied from title/body keywords |
| Strategic labels without milestone | Comment prompting author to add milestone label |

**PR-specific**: Checks linked issues for milestone labels and reports milestone coverage in workflow summary.

### `cross-repo-milestone-sync.yml` - Organization-Wide Enforcement

**Triggers**: Daily at 8:00 UTC; manual with optional target repo and dry-run

| Action | Effect |
|---|---|
| Fetches all org repos (public + private) | Enumerates via `gh repo list` with `GH_PAT` |
| Scans all open issues/PRs per repo | Checks title/body for M*/T* patterns |
| Auto-applies milestone/task labels | Adds `milestone: M0`-`M6`, `task: T1`-`T9` |
| Generates per-repo report | Summary with items checked, labels applied |

This workflow ensures milestone/task labels are enforced across **all** org repos, not just `.github`.

### `doc-staleness-audit.yml` - Document Review

**Triggers**: Weekly Monday at 9:00 UTC

| Action | Labels Used |
|---|---|
| Creates issues for stale docs | Applies `type: documentation` + `status: needs-triage` |

---

## 6. Known Conflicts & Gaps

### CONFLICT 1: Priority LOW vs INFO Mismatch

`labels.yml` defines `🟢Priority:LOW` (manual only) but `auto-label-issues.yml` maps `[low]`/`p4` keywords to `ℹ️Priority:INFO` instead. Users saying "low priority" get `ℹ️Priority:INFO`, never `🟢Priority:LOW`.

**Resolution needed**: Decide which label represents P3/P4 and update either `labels.yml` or the auto-labeling rules for consistency.

### ~~CONFLICT 2: Missing Type Labels in `labels.yml`~~ - RESOLVED

Five `type:` labels were applied by workflows but not defined in `labels.yml`. **Fixed**: All five labels (`type: documentation`, `type: infrastructure`, `type: test`, `type: governance`, `type: security`) have been added to `labels.yml` and will sync org-wide on next Monday or manual trigger.

### CONFLICT 3: Blocked Status Name Mismatch

`quarterly-okr-tracker.yml` searches for `status: blocked` but the actual label in `labels.yml` is `🐌BLOCKED` (different name). The at-risk OKR detection will never find blocked items.

**Resolution needed**: Either update `quarterly-okr-tracker.yml` to search for `🐌BLOCKED`, or add `status: blocked` to `labels.yml` as an alias, or rename the label.

### CONFLICT 4: Priority Label Case Mismatch in Goal Alignment

`goal-alignment-check.yml` checks for `priority: critical` and `priority: high` (lowercase, with space after colon) using `.includes()`. The actual labels are `🚨Priority:CRITICAL` and `🔴Priority:HIGH` (uppercase, no space). The `.includes()` on lowercase label names will match because the comparison is against `l.name` which contains the mixed-case emoji labels and `.includes('priority: critical')` won't match `🚨Priority:CRITICAL`.

**Resolution needed**: Update `goal-alignment-check.yml` to match actual label names (e.g., `Priority:CRITICAL`) or use case-insensitive comparison.

### GAP 1: `labels.json` Redundancy

All 27 labels in `labels.json` are duplicated in `labels.yml`. The shell scripts (`apply-labels.sh`, `apply-labels-gh.sh`) are now redundant since `sync-labels.yml` handles org-wide sync.

**Resolution needed**: Deprecate `labels.json` and shell scripts, or document them as "initial setup" tools only.

### GAP 2: No Auto-Labeling for Database

`area: database` is defined in `labels.yml` but has no auto-labeling rule in `auto-label-issues.yml`. Consider adding keywords like `database`, `db`, `migration`, `schema`.

### GAP 3: Quarter Labels Are Manual Only

Quarter labels (`quarter: Q1`, etc.) and year labels (`2026`) are never auto-applied. All OKR tracking depends on maintainers manually adding these labels. Consider adding template-driven auto-application for issues created from goal/project proposal templates.

---

## 7. Maintenance & Application

### Editing Labels

To add or modify a label:

1. Edit `.github/labels.yml` (the authoritative source)
2. The `sync-labels.yml` workflow will automatically sync to all repos on next Monday, on push to `labels.yml`, or via manual trigger
3. Update this document (`LABELS_README.md`) in the same PR

### Editing Auto-Labeling Rules

To change which keywords trigger which labels:

1. Edit `.github/workflows/auto-label-issues.yml`
2. Update the corresponding entry in this document (Section 4)
3. Update `.github/workflows/README.md`
4. Test on a draft issue before merging

### Adding a New Label

Checklist for adding a new label:

- [ ] Add to `.github/labels.yml` with name, description, and color
- [ ] If auto-applied: add rules to `auto-label-issues.yml`
- [ ] If it triggers downstream workflows: verify `add-to-milestone.yml`, `goal-alignment-check.yml`, `quarterly-okr-tracker.yml` handle it correctly
- [ ] Update this document with the new label entry
- [ ] Run `sync-labels.yml` manually or wait for next Monday sync

### Manual Application

For repos that need labels before the next sync:

```bash
# Using GitHub CLI (recommended)
gh label create "LABEL-NAME" --description "Description" --color "hexcolor" --repo Fused-Gaming/REPO

# Or trigger sync manually
gh workflow run sync-labels.yml --repo Fused-Gaming/.github
```

---

## Related Documents

- [`.github/labels.yml`](.github/labels.yml) - Primary label definitions (83 labels)
- [`labels.json`](labels.json) - Legacy label definitions (27 labels)
- [`.github/workflows/auto-label-issues.yml`](.github/workflows/auto-label-issues.yml) - Auto-labeling workflow
- [`.github/workflows/sync-labels.yml`](.github/workflows/sync-labels.yml) - Label sync workflow
- [`.github/workflows/milestone-task-enforcement.yml`](.github/workflows/milestone-task-enforcement.yml) - Milestone/task enforcement
- [`.github/workflows/cross-repo-milestone-sync.yml`](.github/workflows/cross-repo-milestone-sync.yml) - Cross-repo milestone sync
- [`.github/workflows/add-to-milestone.yml`](.github/workflows/add-to-milestone.yml) - Milestone assignment
- [`.github/workflows/goal-alignment-check.yml`](.github/workflows/goal-alignment-check.yml) - Goal alignment
- [`.github/workflows/quarterly-okr-tracker.yml`](.github/workflows/quarterly-okr-tracker.yml) - OKR tracking
- [`.github/workflows/README.md`](.github/workflows/README.md) - Workflow documentation
- [`DOCUMENT_CLASSIFICATION_POLICY.md`](../governance/DOCUMENT_CLASSIFICATION_POLICY.md) - Document governance

---

**Maintained by**: Core Team / DevOps Lead
**Update Trigger**: On any change to `labels.yml`, `auto-label-issues.yml`, or downstream workflows
