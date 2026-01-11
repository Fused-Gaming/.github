# Repository Labels Guide

This directory contains configuration and scripts for managing repository labels that enhance transparency and facilitate stakeholder communication across all Fused Gaming projects.

## 📋 Contents

- `labels.json` - Complete label definitions organized by phase
- `apply-labels.sh` - Script to apply labels using GitHub API (requires token)
- `apply-labels-gh.sh` - Script to apply labels using GitHub CLI (requires gh)

## 🎯 Label Categories

### Phase 1: Core Transparency
Essential labels for stakeholder communication and visibility.

| Label | Color | Purpose |
|-------|-------|---------|
| 📢ANNOUNCEMENT | ![#0e8a16](https://via.placeholder.com/15/0e8a16/000000?text=+) `#0e8a16` | Public stakeholder announcements |
| 📝CHANGELOG | ![#1d76db](https://via.placeholder.com/15/1d76db/000000?text=+) `#1d76db` | Should appear in public changelog |
| 🎮PLAYER-IMPACT | ![#e99695](https://via.placeholder.com/15/e99695/000000?text=+) `#e99695` | Directly impacts players |
| 💥BREAKING-CHANGE | ![#b60205](https://via.placeholder.com/15/b60205/000000?text=+) `#b60205` | Breaking changes |

### Phase 2: Deployment Visibility
Track deployment status and pipeline stages.

| Label | Color | Purpose |
|-------|-------|---------|
| 🚀READY-FOR-DEPLOY | ![#0e8a16](https://via.placeholder.com/15/0e8a16/000000?text=+) `#0e8a16` | Ready for deployment |
| ✅PRODUCTION | ![#0e8a16](https://via.placeholder.com/15/0e8a16/000000?text=+) `#0e8a16` | Live in production |
| 🔄STAGING | ![#fbca04](https://via.placeholder.com/15/fbca04/000000?text=+) `#fbca04` | In staging environment |

### Phase 3: Security & Trust
Critical labels for building stakeholder trust in the gaming industry.

| Label | Color | Purpose |
|-------|-------|---------|
| 🔒SECURITY | ![#d93f0b](https://via.placeholder.com/15/d93f0b/000000?text=+) `#d93f0b` | Security-related issues/changes |
| 🛡️AUDIT | ![#5319e7](https://via.placeholder.com/15/5319e7/000000?text=+) `#5319e7` | Needs security/compliance audit |
| 🔐COMPLIANCE | ![#b60205](https://via.placeholder.com/15/b60205/000000?text=+) `#b60205` | Regulatory compliance matters |

### Phase 4: Process Enhancement
Improve workflow visibility and status tracking.

| Label | Color | Purpose |
|-------|-------|---------|
| 🎯IN-PROGRESS | ![#c2e0c6](https://via.placeholder.com/15/c2e0c6/000000?text=+) `#c2e0c6` | Currently being worked on |
| ⏳WAITING | ![#fef2c0](https://via.placeholder.com/15/fef2c0/000000?text=+) `#fef2c0` | Waiting on external response |
| 💬DISCUSSION | ![#cc317c](https://via.placeholder.com/15/cc317c/000000?text=+) `#cc317c` | Open for community/stakeholder discussion |
| 🔥HOTFIX | ![#d93f0b](https://via.placeholder.com/15/d93f0b/000000?text=+) `#d93f0b` | Urgent production fix |

### Additional Quality & Workflow Labels
Comprehensive labels for quality assurance and workflow management.

| Label | Color | Purpose |
|-------|-------|---------|
| 🔍INVESTIGATING | ![#d4c5f9](https://via.placeholder.com/15/d4c5f9/000000?text=+) `#d4c5f9` | Under investigation |
| ✨FEATURE | ![#a2eeef](https://via.placeholder.com/15/a2eeef/000000?text=+) `#a2eeef` | New feature development |
| ♻️REFACTOR | ![#c5def5](https://via.placeholder.com/15/c5def5/000000?text=+) `#c5def5` | Code refactoring |
| 📈IMPROVEMENT | ![#84b6eb](https://via.placeholder.com/15/84b6eb/000000?text=+) `#84b6eb` | Performance/quality improvement |
| 💼BUSINESS-DECISION | ![#d4c5f9](https://via.placeholder.com/15/d4c5f9/000000?text=+) `#d4c5f9` | Requires business decision |
| 📊REPORTING | ![#bfdadc](https://via.placeholder.com/15/bfdadc/000000?text=+) `#bfdadc` | For stakeholder reports |
| 💡NEEDS-SPEC | ![#f9d0c4](https://via.placeholder.com/15/f9d0c4/000000?text=+) `#f9d0c4` | Needs detailed specification |
| 🧪TESTING | ![#d4c5f9](https://via.placeholder.com/15/d4c5f9/000000?text=+) `#d4c5f9` | Testing-related |
| ✅VERIFIED | ![#0e8a16](https://via.placeholder.com/15/0e8a16/000000?text=+) `#0e8a16` | Tested and verified |
| 🐛REGRESSION | ![#ee0701](https://via.placeholder.com/15/ee0701/000000?text=+) `#ee0701` | Regression bug |
| 🟢Priority:LOW | ![#0e8a16](https://via.placeholder.com/15/0e8a16/000000?text=+) `#0e8a16` | P3 - LOW priority |
| 👀NEEDS-REVIEW | ![#fbca04](https://via.placeholder.com/15/fbca04/000000?text=+) `#fbca04` | Requires stakeholder review |
| 🏷️RELEASE | ![#5319e7](https://via.placeholder.com/15/5319e7/000000?text=+) `#5319e7` | Release-related items |

## 🚀 How to Apply Labels

### Option 1: Using GitHub CLI (Recommended)

If you have the GitHub CLI installed and authenticated:

```bash
cd /path/to/.github
./apply-labels-gh.sh
```

Or for a different repository:

```bash
./apply-labels-gh.sh owner/repo-name
```

**Prerequisites:**
- Install GitHub CLI: https://cli.github.com/
- Authenticate: `gh auth login`

### Option 2: Using GitHub Token

If you don't have the GitHub CLI:

```bash
cd /path/to/.github
./apply-labels.sh YOUR_GITHUB_TOKEN
```

Or for a different repository:

```bash
./apply-labels.sh YOUR_GITHUB_TOKEN owner/repo-name
```

**Prerequisites:**
- Create a GitHub token: https://github.com/settings/tokens
- Required scopes: `repo` (or `public_repo` for public repositories)

### Option 3: Manual Application

1. Go to your repository on GitHub
2. Navigate to **Issues** → **Labels**
3. Click **New label** for each entry in `labels.json`
4. Copy the name, color (without #), and description

## 📊 Benefits for Stakeholders

### Transparency
- **📢ANNOUNCEMENT** and **📝CHANGELOG** ensure stakeholders see important updates
- **🎮PLAYER-IMPACT** highlights changes that directly affect users
- **📊REPORTING** makes it easy to filter items for stakeholder reports

### Security & Trust
- **🔒SECURITY**, **🛡️AUDIT**, and **🔐COMPLIANCE** demonstrate commitment to security
- Critical for building trust in the gaming industry
- Shows due diligence and regulatory awareness

### Visibility
- **🚀READY-FOR-DEPLOY**, **✅PRODUCTION**, **🔄STAGING** show deployment pipeline
- **🎯IN-PROGRESS** and **🗺️PLANNED** (existing) show work status
- **⏳WAITING** explains delays transparently

### Quality Assurance
- **✅VERIFIED** and **🧪TESTING** show quality commitment
- **🐛REGRESSION** vs **bug** (existing) helps track issue types
- **📈IMPROVEMENT** shows continuous enhancement

## 🔄 Applying to Multiple Repositories

To apply these labels across all Fused Gaming repositories:

```bash
# Using gh CLI
for repo in drift leaderboards gambarewards gambareload vln; do
    ./apply-labels-gh.sh Fused-Gaming/$repo
done

# Or using token
for repo in drift leaderboards gambarewards gambareload vln; do
    ./apply-labels.sh YOUR_TOKEN Fused-Gaming/$repo
done
```

## 📝 Customization

To add or modify labels:

1. Edit `labels.json`
2. Follow the existing structure:
   ```json
   {
     "name": "LABEL-NAME",
     "color": "hexcolor",
     "description": "Description here"
   }
   ```
3. Run the apply script again (existing labels won't be duplicated)

## 🎯 Best Practices

1. **Consistency**: Use these labels consistently across all repositories
2. **Combinations**: Use multiple labels (e.g., `🔒SECURITY` + `🚨Priority:CRITICAL`)
3. **Updates**: Mark `📝CHANGELOG` items for release notes
4. **Communication**: Use `📢ANNOUNCEMENT` for stakeholder-facing changes
5. **Transparency**: Tag `🎮PLAYER-IMPACT` on anything affecting users

## 📖 Integration with Existing Labels

These new labels complement your existing label system:

- **Priority System**: Complete with 🟢Priority:LOW (P0-P4 now complete)
- **Projects**: Work alongside ☕DRIFT, 🏆LEADERBOARDS, etc.
- **Teams**: Coordinate with 👷DEV, 🎨DESIGN, etc.
- **Governance**: Integrate with ❎GOVERNANCE and voting labels
- **Status**: Enhance 🗺️PLANNED, 🎯IN-PROGRESS, ✅COMPLETED workflow

## 🆘 Troubleshooting

**Script fails with "command not found":**
- Ensure the script is executable: `chmod +x apply-labels-gh.sh`
- Check you're in the correct directory

**Authentication errors:**
- For `apply-labels-gh.sh`: Run `gh auth login`
- For `apply-labels.sh`: Verify your token has the correct scopes

**"Label already exists" messages:**
- This is normal - the script skips existing labels
- To update existing labels, delete them first on GitHub

**Python errors:**
- Ensure Python 3 is installed: `python3 --version`

## 📞 Support

For issues or questions about this labeling system, please open an issue in the Fused-Gaming/.github repository.

---

**Total New Labels**: 27
**Organized in**: 5 Phases
**Purpose**: Enhanced transparency and stakeholder trust
