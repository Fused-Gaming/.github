# Documentation Structure Proposal
## Organized Documentation Directory for Fused Gaming

**Created**: February 6, 2026
**Status**: Proposal
**Classification**: INTERNAL

---

## Executive Summary

This proposal reorganizes the `.github` repository to improve discoverability, maintainability, and compliance with documentation best practices. The structure moves detailed documentation into a `docs/` directory while keeping only essential standard files in the repository root.

---

## Current State Issues

**Problems**:
1. ✗ 20+ markdown files in root directory (cluttered)
2. ✗ Difficult to find specific documentation
3. ✗ No clear hierarchy for document types
4. ✗ Mixed concerns (governance, operations, investor, technical)
5. ✗ Hard for new contributors to navigate

**Impact**: Reduced discoverability, harder maintenance, confusion for new contributors

---

## Proposed Structure

### Repository Root (Essential Files Only)

```
/.github/
├── README.md                          ← Organization overview & quick links
├── LICENSE                            ← Repository license
├── SECURITY.md                        ← Security policy (standard location)
├── CONTRIBUTING.md                    ← How to contribute (standard location)
├── CODE_OF_CONDUCT.md                 ← Community standards (to be created)
├── CHANGELOG.md                       ← Version history (to be created)
├── QUICKSTART.md                      ← Quick start guide (optional)
│
├── .gitignore                         ← Git ignore rules
├── .editorconfig                      ← Editor configuration
├── .prettierrc.json                   ← Code formatting rules
├── requirements.txt                   ← Python dependencies
│
├── .github/                           ← GitHub-specific configs (standard)
│   ├── workflows/                     ← GitHub Actions
│   │   ├── *.yml                      ← Workflow files
│   │   └── README.md                  ← Workflow documentation
│   ├── ISSUE_TEMPLATE/                ← Issue templates (standard location)
│   │   ├── bug-report.yml
│   │   ├── feature-request.yml
│   │   ├── goal-proposal.yml
│   │   ├── governance-proposal.yml
│   │   ├── project-proposal.yml
│   │   └── config.yml
│   ├── PULL_REQUEST_TEMPLATE.md       ← PR template (standard location)
│   └── FUNDING.yml                    ← Sponsorship info (to be created)
│
├── docs/                              ← ⭐ All detailed documentation HERE
│   └── (see detailed structure below)
│
├── scripts/                           ← Utility scripts
│   ├── apply-labels.sh
│   ├── apply-labels-gh.sh
│   └── tictactoe.py
│
├── assets/                            ← Images, icons, media
│   └── (existing assets)
│
└── profile/                           ← GitHub profile content
    └── (tic-tac-toe game assets)
```

---

## Detailed `docs/` Directory Structure

```
docs/
│
├── README.md                          ← Documentation hub with index & links
│
├── governance/                        ← Governance & decision-making
│   ├── README.md                      ← Governance overview
│   ├── GOVERNANCE.md                  ← Framework (from root)
│   ├── GOVERNANCE_PROTOCOL.md         ← Detailed protocols (from root)
│   ├── DOCUMENT_CLASSIFICATION_POLICY.md  ← Info classification (from root)
│   ├── CODE_OF_CONDUCT.md             ← Community standards
│   └── DECISION_LOG.md                ← Major decisions record (to be created)
│
├── planning/                          ← Strategic planning & goals
│   ├── README.md                      ← Planning overview
│   ├── GOALS.md                       ← Strategic goals (from root)
│   ├── MILESTONES_OVERVIEW.md         ← Milestones tracking (from root)
│   ├── ROADMAP.md                     ← Product roadmap (to be created)
│   └── quarterly/                     ← Quarterly OKR tracking
│       ├── 2026-Q1.md
│       ├── 2026-Q2.md
│       └── ...
│
├── operations/                        ← Day-to-day operations
│   ├── README.md                      ← Operations overview
│   ├── PROJECT_BOARD_GUIDE.md         ← Project tracking (from root)
│   ├── WORKSPACE_GUIDE.md             ← Workspace setup (from root)
│   ├── LABELS_README.md               ← Label system (from root)
│   ├── WORKFLOWS_GUIDE.md             ← GitHub Actions guide (to be created)
│   └── RELEASE_PROCESS.md             ← Release procedures (to be created)
│
├── business/                          ← Business & investor relations
│   ├── README.md                      ← Business docs overview
│   ├── INVESTOR_DASHBOARD_PUBLIC.md   ← Public dashboard (from root)
│   ├── INVESTOR_COMMUNICATIONS_STRATEGY.md  ← Strategy (from root)
│   ├── SIMPLIFIED_INVESTOR_SOLUTION.md     ← Implementation (from root)
│   ├── JOB_OPPORTUNITIES_SUMMARY.md   ← Contractor roles (from root)
│   └── PARTNERSHIP_GUIDELINES.md      ← Partnership approach (to be created)
│
├── technical/                         ← Technical documentation
│   ├── README.md                      ← Technical docs overview
│   ├── ARCHITECTURE.md                ← System architecture (to be created)
│   ├── API_DESIGN.md                  ← API guidelines (to be created)
│   ├── SECURITY_GUIDELINES.md         ← Security best practices (to be created)
│   ├── TESTING_STRATEGY.md            ← Testing approach (to be created)
│   └── DEPLOYMENT.md                  ← Deployment procedures (to be created)
│
├── community/                         ← Community engagement
│   ├── README.md                      ← Community overview
│   ├── ONBOARDING.md                  ← New contributor guide (to be created)
│   ├── RECOGNITION.md                 ← Contributor recognition (to be created)
│   ├── EVENTS.md                      ← Community events (to be created)
│   └── FAQ.md                         ← Frequently asked questions (to be created)
│
├── projects/                          ← Individual project documentation
│   ├── README.md                      ← Projects overview
│   ├── PORTFOLIO.md                   ← Complete portfolio (to be created)
│   ├── drift/                         ← DRIFT Discord bot
│   │   ├── README.md
│   │   ├── ARCHITECTURE.md
│   │   └── API.md
│   ├── gamba-rewards/                 ← GambaRewards blockchain
│   │   ├── README.md
│   │   ├── SMART_CONTRACTS.md
│   │   └── SECURITY.md
│   ├── gamba-reload/                  ← GambaReload web app
│   ├── leaderboards/                  ← Leaderboards platform
│   └── vln/                           ← VLN AI infrastructure
│
├── templates/                         ← Document templates
│   ├── README.md                      ← Templates overview
│   ├── PROJECT_README_TEMPLATE.md     ← Project README template
│   ├── PROPOSAL_TEMPLATE.md           ← Proposal template
│   ├── RFC_TEMPLATE.md                ← Request for comments
│   └── MEETING_NOTES_TEMPLATE.md      ← Meeting notes
│
├── audit/                             ← Audit reports & recommendations
│   ├── README.md                      ← Audit overview
│   ├── ORG_AUDIT_RECOMMENDATIONS.md   ← Current audit (from root)
│   └── archive/                       ← Historical audits
│       └── ...
│
└── archive/                           ← Deprecated/historical docs
    ├── README.md                      ← Archive overview
    └── YYYY-MM-DD_filename.md         ← Dated archived docs
```

---

## File Classification & Movement Plan

### Keep in Root (13 files)

| File | Reason | Status |
|------|--------|--------|
| `README.md` | Entry point, essential | ✅ Keep |
| `LICENSE` | Standard location | ✅ Keep |
| `SECURITY.md` | Standard location, GitHub looks here | ✅ Keep |
| `CONTRIBUTING.md` | Standard location, GitHub looks here | ✅ Keep |
| `CODE_OF_CONDUCT.md` | Standard location (to be created) | 🔴 Create |
| `CHANGELOG.md` | Standard location (optional) | 🔴 Create |
| `QUICKSTART.md` | Quick reference (optional) | 🔴 Create |
| `.gitignore` | Git configuration | ✅ Keep |
| `.editorconfig` | Editor configuration | ✅ Keep |
| `.prettierrc.json` | Formatting configuration | ✅ Keep |
| `requirements.txt` | Python dependencies | ✅ Keep |
| `PULL_REQUEST_TEMPLATE.md` | In `.github/` (standard) | ✅ Keep |
| `Fused` | Unknown file - review needed | ⚠️ Review |

### Move to `docs/governance/` (4 files)

| Current Location | New Location | Action |
|-----------------|--------------|--------|
| `GOVERNANCE.md` | `docs/governance/GOVERNANCE.md` | 🔄 Move |
| `GOVERNANCE_PROTOCOL.md` | `docs/governance/GOVERNANCE_PROTOCOL.md` | 🔄 Move |
| `DOCUMENT_CLASSIFICATION_POLICY.md` | `docs/governance/DOCUMENT_CLASSIFICATION_POLICY.md` | 🔄 Move |
| (to be created) | `docs/governance/CODE_OF_CONDUCT.md` | 🔴 Create |

### Move to `docs/planning/` (2 files)

| Current Location | New Location | Action |
|-----------------|--------------|--------|
| `GOALS.md` | `docs/planning/GOALS.md` | 🔄 Move |
| `MILESTONES_OVERVIEW.md` | `docs/planning/MILESTONES_OVERVIEW.md` | 🔄 Move |

### Move to `docs/operations/` (3 files)

| Current Location | New Location | Action |
|-----------------|--------------|--------|
| `PROJECT_BOARD_GUIDE.md` | `docs/operations/PROJECT_BOARD_GUIDE.md` | 🔄 Move |
| `WORKSPACE_GUIDE.md` | `docs/operations/WORKSPACE_GUIDE.md` | 🔄 Move |
| `LABELS_README.md` | `docs/operations/LABELS_README.md` | 🔄 Move |

### Move to `docs/business/` (4 files)

| Current Location | New Location | Action |
|-----------------|--------------|--------|
| `INVESTOR_DASHBOARD_PUBLIC.md` | `docs/business/INVESTOR_DASHBOARD_PUBLIC.md` | 🔄 Move |
| `INVESTOR_COMMUNICATIONS_STRATEGY.md` | `docs/business/INVESTOR_COMMUNICATIONS_STRATEGY.md` | 🔄 Move |
| `SIMPLIFIED_INVESTOR_SOLUTION.md` | `docs/business/SIMPLIFIED_INVESTOR_SOLUTION.md` | 🔄 Move |
| `JOB_OPPORTUNITIES_SUMMARY.md` | `docs/business/JOB_OPPORTUNITIES_SUMMARY.md` | 🔄 Move |

### Move to `docs/audit/` (1 file)

| Current Location | New Location | Action |
|-----------------|--------------|--------|
| `ORG_AUDIT_RECOMMENDATIONS.md` | `docs/audit/ORG_AUDIT_RECOMMENDATIONS.md` | 🔄 Move |

### Move to `scripts/` (4 files)

| Current Location | New Location | Action |
|-----------------|--------------|--------|
| `apply-labels.sh` | `scripts/apply-labels.sh` | 🔄 Move |
| `apply-labels-gh.sh` | `scripts/apply-labels-gh.sh` | 🔄 Move |
| `script.sh` | `scripts/utility.sh` or delete | ⚠️ Review |
| `tictactoe.py` | `scripts/tictactoe.py` or `profile/tictactoe.py` | 🔄 Move |

### Move to `profile/` or `assets/` (3 files)

| Current Location | New Location | Action |
|-----------------|--------------|--------|
| `game_state.json` | `profile/game_state.json` | 🔄 Move |
| `tile_count.json` | `profile/tile_count.json` | 🔄 Move |
| `labels.json` | `scripts/labels.json` or `.github/labels.json` | 🔄 Move |

---

## New Root README.md Structure

The root README.md should become a navigation hub:

```markdown
# Fused Gaming 🎮

Welcome to Fused Gaming's organization repository! This repo contains governance, documentation, and community resources for the Fused Gaming ecosystem.

## Quick Links

- 📖 [Documentation Hub](docs/README.md)
- 🤝 [Contributing Guide](CONTRIBUTING.md)
- 🔒 [Security Policy](SECURITY.md)
- 📋 [Code of Conduct](CODE_OF_CONDUCT.md)
- 🎯 [Strategic Goals](docs/planning/GOALS.md)
- 👥 [Community](docs/community/README.md)

## About

[Brief description - 2-3 paragraphs]

## Documentation

All detailed documentation is organized in the [`docs/`](docs/) directory:

- **[Governance](docs/governance/)** - How we make decisions
- **[Planning](docs/planning/)** - Goals, milestones, roadmaps
- **[Operations](docs/operations/)** - Day-to-day processes
- **[Business](docs/business/)** - Investor relations, partnerships
- **[Technical](docs/technical/)** - Architecture, APIs, deployment
- **[Community](docs/community/)** - Onboarding, events, recognition
- **[Projects](docs/projects/)** - Individual project documentation

## Get Started

1. Read the [Quick Start Guide](QUICKSTART.md)
2. Review [Contributing Guidelines](CONTRIBUTING.md)
3. Join our [Telegram](https://t.me/fusedgg)
4. Check out [Good First Issues](https://github.com/Fused-Gaming/.github/labels/good%20first%20issue)

## Projects

See our [Project Portfolio](docs/projects/PORTFOLIO.md) for details on all 35+ repositories.

**Flagship Projects**:
- [DRIFT](docs/projects/drift/) - Discord community bot
- [GambaRewards](docs/projects/gamba-rewards/) - Blockchain rewards
- [GambaReload](docs/projects/gamba-reload/) - Gaming credit management
- [Leaderboards](docs/projects/leaderboards/) - Competitive rankings
- [VLN](docs/projects/vln/) - AI/ML analytics

## Contact

- 💬 Telegram: [@fusedgg](https://t.me/fusedgg)
- 🐦 Twitter: [@fuseddotgg](https://x.com/fuseddotgg)
- 💼 LinkedIn: [Fused Gaming](https://www.linkedin.com/company/fusedgg/)

---

**License**: [LICENSE](LICENSE) | **Last Updated**: February 2026
```

---

## New `docs/README.md` (Documentation Hub)

```markdown
# Fused Gaming Documentation

Welcome to the Fused Gaming documentation hub! This directory contains all detailed documentation for the organization.

## Documentation Categories

### 📋 [Governance](governance/)
How we make decisions, document classification, and organizational structure.

**Key Documents**:
- [Governance Framework](governance/GOVERNANCE.md)
- [Governance Protocols](governance/GOVERNANCE_PROTOCOL.md)
- [Document Classification Policy](governance/DOCUMENT_CLASSIFICATION_POLICY.md)

### 🎯 [Planning](planning/)
Strategic goals, milestones, and roadmaps.

**Key Documents**:
- [2026 Strategic Goals](planning/GOALS.md)
- [Milestones Overview](planning/MILESTONES_OVERVIEW.md)
- [Quarterly OKRs](planning/quarterly/)

### ⚙️ [Operations](operations/)
Day-to-day operational processes and guides.

**Key Documents**:
- [Project Board Guide](operations/PROJECT_BOARD_GUIDE.md)
- [Workspace Guide](operations/WORKSPACE_GUIDE.md)
- [Label System](operations/LABELS_README.md)

### 💼 [Business](business/)
Investor relations, partnerships, and business development.

**Key Documents**:
- [Investor Dashboard (Public)](business/INVESTOR_DASHBOARD_PUBLIC.md)
- [Investor Communications Strategy](business/INVESTOR_COMMUNICATIONS_STRATEGY.md)
- [Job Opportunities](business/JOB_OPPORTUNITIES_SUMMARY.md)

### 🔧 [Technical](technical/)
Architecture, APIs, security, and deployment documentation.

**Key Documents**:
- [Architecture Overview](technical/ARCHITECTURE.md) *(to be created)*
- [API Design Guidelines](technical/API_DESIGN.md) *(to be created)*
- [Security Guidelines](technical/SECURITY_GUIDELINES.md) *(to be created)*

### 👥 [Community](community/)
Community engagement, onboarding, and recognition.

**Key Documents**:
- [Onboarding Guide](community/ONBOARDING.md) *(to be created)*
- [Contributor Recognition](community/RECOGNITION.md) *(to be created)*
- [Community FAQ](community/FAQ.md) *(to be created)*

### 🚀 [Projects](projects/)
Individual project documentation and portfolio.

**Key Documents**:
- [Project Portfolio](projects/PORTFOLIO.md) *(to be created)*
- [DRIFT](projects/drift/)
- [GambaRewards](projects/gamba-rewards/)
- [GambaReload](projects/gamba-reload/)
- [Leaderboards](projects/leaderboards/)
- [VLN](projects/vln/)

### 📄 [Templates](templates/)
Document templates for consistency.

**Available Templates**:
- [Project README Template](templates/PROJECT_README_TEMPLATE.md)
- [Proposal Template](templates/PROPOSAL_TEMPLATE.md)
- [RFC Template](templates/RFC_TEMPLATE.md)

### 🔍 [Audit](audit/)
Audit reports and recommendations.

**Recent Audits**:
- [Organization Audit Recommendations](audit/ORG_AUDIT_RECOMMENDATIONS.md)

---

## Finding Documentation

### By Topic
- **Starting out?** → [Community Onboarding](community/ONBOARDING.md)
- **Want to contribute?** → [Contributing Guide](../CONTRIBUTING.md)
- **Need to propose something?** → [Governance](governance/)
- **Looking for project info?** → [Projects](projects/)
- **Investor inquiries?** → [Business](business/)

### By Role
- **New Contributor**: Start with [Onboarding](community/ONBOARDING.md)
- **Developer**: Check [Technical](technical/) and [Projects](projects/)
- **Investor**: See [Business](business/)
- **Core Team**: Review [Governance](governance/) and [Planning](planning/)

---

## Document Maintenance

All documents follow our [Document Classification Policy](governance/DOCUMENT_CLASSIFICATION_POLICY.md).

**Update Frequency**:
- **Monthly**: Planning documents (GOALS.md, dashboards)
- **Quarterly**: Strategic reviews, governance
- **As Needed**: Technical docs, project docs
- **Continuous**: Community docs, FAQs

**Last Updated**: February 2026
```

---

## Migration Plan

### Phase 1: Create Structure (Week 1)

**Tasks**:
- [ ] Create `docs/` directory and all subdirectories
- [ ] Create README.md files for each subdirectory
- [ ] Create `scripts/` directory
- [ ] Set up directory structure per proposal

**Timeline**: 1-2 days

### Phase 2: Move Existing Files (Week 1-2)

**Tasks**:
- [ ] Move governance docs to `docs/governance/`
- [ ] Move planning docs to `docs/planning/`
- [ ] Move operations docs to `docs/operations/`
- [ ] Move business docs to `docs/business/`
- [ ] Move audit docs to `docs/audit/`
- [ ] Move scripts to `scripts/`
- [ ] Move profile/game files appropriately

**Timeline**: 2-3 days

### Phase 3: Update Links (Week 2)

**Tasks**:
- [ ] Update all internal links in moved documents
- [ ] Update links in root README.md
- [ ] Update links in CONTRIBUTING.md
- [ ] Update links in GitHub issue templates
- [ ] Update links in PR template
- [ ] Update links in workflow files

**Timeline**: 1-2 days

### Phase 4: Create New Root README (Week 2)

**Tasks**:
- [ ] Write new concise root README.md with navigation
- [ ] Create docs/README.md as documentation hub
- [ ] Create subdirectory README.md files
- [ ] Add navigation breadcrumbs

**Timeline**: 1 day

### Phase 5: Create Missing Documents (Week 3-4)

**Priority P0** (Create immediately):
- [ ] `CODE_OF_CONDUCT.md`
- [ ] `docs/community/ONBOARDING.md`
- [ ] `docs/community/FAQ.md`

**Priority P1** (Create soon):
- [ ] `QUICKSTART.md`
- [ ] `docs/projects/PORTFOLIO.md`
- [ ] `docs/technical/ARCHITECTURE.md`

**Priority P2** (Create when needed):
- [ ] `CHANGELOG.md`
- [ ] `docs/planning/ROADMAP.md`
- [ ] `docs/technical/API_DESIGN.md`
- [ ] `docs/technical/TESTING_STRATEGY.md`

**Timeline**: 1-2 weeks

### Phase 6: Update Automation (Week 3)

**Tasks**:
- [ ] Update `doc-freshness-check.yml` for new paths
- [ ] Update `doc-staleness-audit.yml` for new structure
- [ ] Update any scripts referencing old paths
- [ ] Test all GitHub Actions workflows

**Timeline**: 1-2 days

---

## Link Update Strategy

### Automated Link Updates

Create a script to update all internal links:

```bash
#!/bin/bash
# update-doc-links.sh

# Map of old paths to new paths
declare -A path_map=(
  ["GOVERNANCE.md"]="docs/governance/GOVERNANCE.md"
  ["GOVERNANCE_PROTOCOL.md"]="docs/governance/GOVERNANCE_PROTOCOL.md"
  ["DOCUMENT_CLASSIFICATION_POLICY.md"]="docs/governance/DOCUMENT_CLASSIFICATION_POLICY.md"
  ["GOALS.md"]="docs/planning/GOALS.md"
  ["MILESTONES_OVERVIEW.md"]="docs/planning/MILESTONES_OVERVIEW.md"
  ["PROJECT_BOARD_GUIDE.md"]="docs/operations/PROJECT_BOARD_GUIDE.md"
  ["WORKSPACE_GUIDE.md"]="docs/operations/WORKSPACE_GUIDE.md"
  ["LABELS_README.md"]="docs/operations/LABELS_README.md"
  ["INVESTOR_DASHBOARD_PUBLIC.md"]="docs/business/INVESTOR_DASHBOARD_PUBLIC.md"
  ["INVESTOR_COMMUNICATIONS_STRATEGY.md"]="docs/business/INVESTOR_COMMUNICATIONS_STRATEGY.md"
  ["SIMPLIFIED_INVESTOR_SOLUTION.md"]="docs/business/SIMPLIFIED_INVESTOR_SOLUTION.md"
  ["JOB_OPPORTUNITIES_SUMMARY.md"]="docs/business/JOB_OPPORTUNITIES_SUMMARY.md"
  ["ORG_AUDIT_RECOMMENDATIONS.md"]="docs/audit/ORG_AUDIT_RECOMMENDATIONS.md"
)

# Update links in all markdown files
for old_path in "${!path_map[@]}"; do
  new_path="${path_map[$old_path]}"
  echo "Updating links: $old_path -> $new_path"

  # Find and replace in all .md files
  find . -name "*.md" -type f -exec sed -i "s|]($old_path)|]($new_path)|g" {} +
  find . -name "*.md" -type f -exec sed -i "s|](/$old_path)|](/$new_path)|g" {} +
done

echo "Link updates complete!"
```

### Manual Review Required

**Files to manually check**:
- `.github/ISSUE_TEMPLATE/*.yml` - Template links
- `.github/PULL_REQUEST_TEMPLATE.md` - PR checklist links
- `.github/workflows/*.yml` - Workflow file paths
- Root `README.md` - All navigation links

---

## Benefits of This Structure

### ✅ Improved Organization
- Clear hierarchy by topic area
- Easy to find related documents
- Logical grouping reduces cognitive load

### ✅ Better Discoverability
- Documentation hub with clear navigation
- Category-based organization
- README.md in each directory explaining contents

### ✅ Scalability
- Room to grow within each category
- Archive directory for old docs
- Templates directory for consistency

### ✅ Maintainability
- Related docs grouped together
- Easier to update related documents
- Clear ownership by category

### ✅ Contributor Friendly
- New contributors can find onboarding easily
- Clear path from root → docs → specific topic
- Templates make contribution easier

### ✅ Professional Appearance
- Clean root directory
- Standard GitHub practices followed
- Enterprise-level organization

---

## Standard Files Reference

### Files That MUST Stay in Root

Per GitHub and industry conventions:

1. **README.md** - Entry point, GitHub displays automatically
2. **LICENSE** - GitHub detects and displays license
3. **SECURITY.md** - GitHub security tab links here
4. **CONTRIBUTING.md** - GitHub contributor guide link
5. **CODE_OF_CONDUCT.md** - GitHub community standards
6. **.gitignore** - Git configuration
7. **package.json** / **requirements.txt** - Dependency files
8. **.github/** directory - GitHub-specific configs

### Optional Standard Files (Can Be in Root)

1. **CHANGELOG.md** - Version history
2. **AUTHORS.md** - Contributors list
3. **QUICKSTART.md** - Quick reference
4. **SUPPORT.md** - Support resources
5. **.editorconfig** - Editor settings
6. **.prettierrc** / **.eslintrc** - Code formatting

### Config Files

Keep configuration files in root:
- `.prettierrc.json`
- `.editorconfig`
- `.eslintrc.js` (if using)
- `tsconfig.json` (if using TypeScript)
- `jest.config.js` (if using Jest)

---

## Implementation Checklist

### Pre-Migration
- [ ] Review this proposal with core team
- [ ] Get approval for structure
- [ ] Create backup branch before migration
- [ ] Announce migration to community

### Migration
- [ ] Create directory structure
- [ ] Move files to new locations
- [ ] Update all internal links
- [ ] Test all links manually
- [ ] Update automation scripts
- [ ] Update GitHub Actions workflows

### Post-Migration
- [ ] Create missing README.md files
- [ ] Write new root README.md
- [ ] Test all workflows
- [ ] Update DOCUMENT_CLASSIFICATION_POLICY.md with new paths
- [ ] Announce completion to community
- [ ] Archive old structure documentation

---

## Risk Mitigation

### Risk: Broken Links

**Mitigation**:
1. Use automated link update script
2. Manual review of all workflows and templates
3. Test in a branch before merging to main
4. Keep a link redirect map for 90 days

### Risk: Workflow Failures

**Mitigation**:
1. Update workflow paths before migration
2. Test each workflow individually
3. Have rollback plan ready

### Risk: Contributor Confusion

**Mitigation**:
1. Announce migration in advance
2. Create migration guide
3. Update CONTRIBUTING.md immediately
4. Pin discussion with new structure

---

## Success Metrics

### Quantitative
- Reduce root directory files from 20+ to ~10
- 100% of links working post-migration
- Zero workflow failures after migration
- All docs have clear category

### Qualitative
- New contributors can find onboarding in < 1 minute
- Documentation is "obviously organized" per feedback
- Core team finds docs faster
- Professional appearance per external review

---

## Alternative Considered: Flat Structure

**Approach**: Keep all docs in root with naming convention (e.g., `GOVERNANCE_FRAMEWORK.md`, `PLANNING_GOALS.md`)

**Pros**:
- Simpler structure
- All docs at one level

**Cons**:
- Still cluttered root
- Harder to navigate with 30+ docs
- Doesn't scale well
- Less professional appearance

**Decision**: Rejected in favor of hierarchical structure

---

## References

- [GitHub Community Standards](https://docs.github.com/en/communities)
- [Open Source Guides](https://opensource.guide/)
- [Documentation Best Practices](https://documentation.divio.com/)
- [Docs as Code](https://www.writethedocs.org/guide/docs-as-code/)

---

## Appendix: Example Organizations

Organizations with excellent documentation structure:

1. **GitLab** - [gitlab.com/gitlab-org/gitlab](https://gitlab.com/gitlab-org/gitlab)
   - `doc/` directory with clear categories
   - Comprehensive navigation

2. **Microsoft Docs** - [github.com/MicrosoftDocs](https://github.com/MicrosoftDocs)
   - Topic-based organization
   - Clear hierarchy

3. **Kubernetes** - [kubernetes.io/docs](https://kubernetes.io/docs)
   - Role-based documentation
   - Getting started paths

4. **Rust** - [rust-lang.org/learn](https://doc.rust-lang.org/)
   - Learning paths
   - Reference documentation

---

## Next Steps

1. **Review & Approve**: Core team reviews this proposal
2. **Create Branch**: `docs-restructure` branch for migration
3. **Implement Phase 1**: Create directory structure
4. **Implement Phase 2**: Move files
5. **Implement Phase 3**: Update links
6. **Test**: Verify all links and workflows
7. **Merge**: Merge to main after testing
8. **Announce**: Communicate new structure

---

## Questions & Feedback

**Questions about this proposal?**
- Open a discussion with label `type: documentation`
- Comment on the PR implementing this structure
- DM on [Telegram](https://t.me/fusedgg)

---

**Status**: Awaiting core team approval
**Created**: February 6, 2026
**Owner**: Core Team
**Next Review**: After implementation

---

_This proposal ensures Fused Gaming has enterprise-level documentation organization while maintaining open-source accessibility._
