# Document Classification & Continuous Update Policy

**Version**: 1.0
**Effective Date**: February 6, 2026
**Next Review**: May 6, 2026
**Status**: Active

---

## Purpose

This policy establishes:
1. A classification system to protect trade secrets and sensitive information in public repositories
2. Enforcement mechanisms to keep living documents current with every significant change
3. Clear boundaries between public transparency and confidential business operations

This policy implements the transparency exceptions defined in [GOVERNANCE_PROTOCOL.md](GOVERNANCE_PROTOCOL.md) Protocol 9.3.

---

## 1. Document Classification Levels

### PUBLIC - Open Information

Documents visible to anyone. Must NOT contain trade secrets, financials, investor details, or stakeholder PII.

| Document | Type | Update Trigger |
|---|---|---|
| `README.md` | Profile | Quarterly or on major org changes |
| `CONTRIBUTING.md` | Process | On process changes |
| `SECURITY.md` | Policy | Semi-annually or on incident |
| `GOVERNANCE.md` | Framework | On governance votes (Protocol 10.1) |
| `GOVERNANCE_PROTOCOL.md` | Protocol | On governance votes (Protocol 10.1) |
| `PROJECT_BOARD_GUIDE.md` | Operational | On every merged PR that changes board structure |
| `GOALS.md` | Strategic | Monthly progress update, quarterly revision |
| `CODE_OF_CONDUCT.md` | Policy | Annually |
| `WORKSPACE_GUIDE.md` | Reference | On tooling changes |
| `LABELS_README.md` | Reference | On label definition or auto-labeling rule changes |
| `.github/workflows/README.md` | Reference | On workflow changes |

**Rule**: Any PR that modifies workflows, labels, templates, or board configuration MUST include corresponding doc updates as part of the PR checklist.

### INTERNAL - Org Members Only

Documents that should live in **private repositories** or GitHub Wiki with restricted access. Contain operational details that are not trade secrets but provide competitive insight.

| Content Type | Current Location | Recommended Location |
|---|---|---|
| Milestone progress with business metrics | `MILESTONES_OVERVIEW.md` (PUBLIC) | Private repo or restricted wiki |
| Detailed OKR tracking with resource allocation | `GOALS.md` (partial) | Separate internal tracker |
| Project health reviews with contributor data | Not yet created | Private repo |
| Bug triage notes with internal priorities | Issue comments | Internal labels + private notes |

### CONFIDENTIAL - Core Team Only

Must NEVER appear in any public repository, commit history, issue, or PR comment.

| Content Type | Risk If Exposed | Where It Should Live |
|---|---|---|
| Investor names, contacts, pitch materials | Competitive, legal | Private repo with restricted access |
| Revenue figures, funding amounts, burn rate | Competitive | Private financial repo |
| Partnership terms, NDA-covered information | Legal liability | Secure document storage (not GitHub) |
| Stakeholder PII (emails, phone numbers) | Privacy violation, GDPR | Encrypted storage, not Git |
| API keys, credentials, wallet private keys | Security breach | Secrets manager (not Git, not env files) |
| Security vulnerabilities (pre-disclosure) | Active exploitation | Private security advisories |

---

## 2. Enforcement Mechanisms

### 2.1 PR Merge Gate - Doc Freshness Check

A GitHub Actions workflow (`doc-freshness-check.yml`) MUST run on every PR to `main`/`master`:

**What it checks:**
- If the PR modifies files in `.github/workflows/`, require updates to `.github/workflows/README.md`
- If the PR modifies `labels.yml`, require updates to `PROJECT_BOARD_GUIDE.md` label sections
- If the PR modifies issue templates, require updates to `PROJECT_BOARD_GUIDE.md` workflow sections
- If the PR closes an issue linked to a milestone, flag `MILESTONES_OVERVIEW.md` for update
- If any classified-public doc has a `Last Updated` date older than 90 days, warn in PR comment

**Enforcement level:** Warning (non-blocking) for first 30 days, then blocking.

### 2.2 Scheduled Staleness Audit

A weekly scheduled workflow (`doc-staleness-audit.yml`) MUST:
- Parse all markdown files for `Last Updated` dates
- Flag any doc past its stated `Next Review` date
- Create an issue titled `[DOC REVIEW] {filename} is past review date` with label `type: documentation`
- Assign to the doc owner or `@core-team`

### 2.3 Sensitive Content Scanner

A pre-merge check (`sensitive-content-scan.yml`) MUST scan PRs for:
- Email addresses not in an approved public list
- Phone numbers
- Dollar amounts with context suggesting financials (e.g., "$X funding", "revenue", "burn rate")
- Keywords: "investor", "pitch", "funding round", "valuation", "NDA", "confidential"
- API key patterns, wallet addresses, credentials

**Action on match:** Block merge, comment with findings, require manual override by core team member.

### 2.4 PR Template Enforcement

The existing `PULL_REQUEST_TEMPLATE.md` MUST include a documentation checklist:

```markdown
## Documentation Impact
- [ ] No documentation updates needed
- [ ] Updated relevant docs (list which ones)
- [ ] Verified no confidential information in changes
- [ ] Updated `Last Updated` date on modified docs
```

---

## 3. Continuous Update Protocol

### On Every Merged PR

The author (or reviewer) is responsible for:

1. **Check**: Does this PR change any process, workflow, template, label, or board structure?
2. **Update**: If yes, update the corresponding public doc(s) in the same PR
3. **Date**: Bump `Last Updated` on every doc modified
4. **Review**: Reviewer verifies doc updates match code changes

### On Every Closed Bug

1. If the bug was tracked on the project board, verify board guide accuracy
2. If the bug revealed a process gap, update CONTRIBUTING.md or relevant process doc
3. If the bug was a security issue, follow SECURITY.md disclosure process

### Monthly

1. Core team reviews all `Last Updated` dates
2. Update GOALS.md OKR progress
3. Run doc staleness audit manually if automated version not yet deployed

### Quarterly

1. Full doc review cycle per GOVERNANCE_PROTOCOL.md Protocol 10.2
2. Rotate `Next Review` dates
3. Archive or deprecate obsolete docs
4. Verify classification levels still appropriate

---

## 4. Immediate Remediation Required

The following content is currently in PUBLIC repos but violates this classification policy:

### MILESTONES_OVERVIEW.md - Contains INTERNAL/CONFIDENTIAL content

| Section | Classification | Action Required |
|---|---|---|
| "Funding and Business Model" (lines 409-422) | CONFIDENTIAL | Remove entirely, move to private repo |
| "Investor Pitch Status: Preparing materials (30% complete)" (line 422) | CONFIDENTIAL | Remove |
| "Potential Revenue Streams" (lines 413-418) | INTERNAL | Move to private repo |
| "Pre-revenue, seeking initial funding" (line 412) | INTERNAL | Remove or generalize |
| Specific issue numbers for investor readiness (#23-#27) (lines 108-112) | INTERNAL | Keep issue refs but remove business context |
| "Key Metrics Dashboard" with TBD business targets (lines 309-336) | INTERNAL | Keep structure, remove financial targets |
| Team structure/roles needed (lines 494-507) | PUBLIC | OK to keep |

### PROJECT_BOARD_GUIDE.md - Contains Stale/Incorrect content

| Section | Issue | Action Required |
|---|---|---|
| Project #10 reference (line 7) | Board doesn't exist | Update to existing board or mark as planned |
| External tools listing Telegram only (line 248) | Incomplete | Update with all actual channels |
| "Last Updated: January 2026" (line 340) | Stale | Update |

---

## 5. Document Ownership Matrix

Every living document MUST have a designated owner responsible for freshness.

| Document | Owner | Update Cadence | Enforcement |
|---|---|---|---|
| `PROJECT_BOARD_GUIDE.md` | Core Team | On board changes + quarterly | PR gate |
| `GOALS.md` | Core Team Lead | Monthly + quarterly | Scheduled audit |
| `MILESTONES_OVERVIEW.md` | Core Team Lead | Monthly | Scheduled audit |
| `GOVERNANCE.md` | Core Team (collective) | On governance votes | Protocol 10.1 |
| `GOVERNANCE_PROTOCOL.md` | Core Team (collective) | On governance votes | Protocol 10.1 |
| `CONTRIBUTING.md` | Any maintainer | On process changes | PR gate |
| `SECURITY.md` | Security lead | Semi-annually | Scheduled audit |
| `ORG_AUDIT_RECOMMENDATIONS.md` | Core Team | Per audit cycle | Manual |
| `LABELS_README.md` | Core Team / DevOps lead | On label or workflow changes | PR gate |
| `.github/workflows/README.md` | DevOps lead | On workflow changes | PR gate |

---

## Related Documents

- [GOVERNANCE_PROTOCOL.md](GOVERNANCE_PROTOCOL.md) - Protocol 9.3 (Transparency Exceptions)
- [SECURITY.md](SECURITY.md) - Security reporting and handling
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution process
- [ORG_AUDIT_RECOMMENDATIONS.md](ORG_AUDIT_RECOMMENDATIONS.md) - Current audit findings

---

**Last Updated**: February 6, 2026
**Next Review**: May 6, 2026
