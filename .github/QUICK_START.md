# Quick Start: Organization-Wide Label Sync

## 🎯 What We Fixed

Your label sync workflow was failing because:
1. ❌ Labels split between `labels.yml` and `labels.json`
2. ❌ Workflows in wrong location (`.github/.github/workflows/`)
3. ❌ Only syncing to current repo, not organization-wide

## ✅ What's Now Ready

1. ✅ **Single source of truth**: All 83 labels in `.github/labels.yml`
2. ✅ **Correct location**: Workflows in `.github/workflows/`
3. ✅ **Org-wide sync**: Matrix strategy to sync all repos in parallel
4. ✅ **VS Code workspace**: Configured for efficient project management
5. ✅ **Documentation**: Complete setup guides and troubleshooting

## ⚡ Next Actions (Required)

### Step 1: Create Personal Access Token

```bash
# Open GitHub token settings
open https://github.com/settings/tokens?type=beta
# Or manually: GitHub Settings → Developer settings → Personal access tokens → Fine-grained
```

Configure token:
- **Name**: Label Sync Token
- **Expiration**: 90 days
- **Repository access**: All repositories
- **Permissions**:
  - Issues: Read and write ✅
  - Metadata: Read-only ✅

### Step 2: Add Token to Repository

```bash
# Go to your repository settings
# Settings → Secrets and variables → Actions → New repository secret
# Name: GH_PAT
# Value: [paste your token]
```

### Step 3: Commit and Push Changes

```bash
cd "K:\git\projects\Fused Gaming"

git add .github/ .vscode/ .editorconfig .prettierrc.json .gitignore README.md WORKSPACE_GUIDE.md
git status  # Review changes

git commit -m "Setup: Configure organization-wide label sync

- Merge all 83 labels into .github/labels.yml
- Fix workflow location and enable org-wide sync
- Add comprehensive documentation
- Configure VS Code workspace"

git push origin main
```

### Step 4: Test the Workflow

```bash
# Test on single repo first (safer)
gh workflow run sync-labels.yml -f target_repo="Fused-Gaming/your-test-repo"

# Or sync entire organization (after testing)
gh workflow run sync-labels.yml

# Monitor progress
gh run watch
```

## 📊 What Happens When You Run

```
Sync Process:
├── Get all org repositories (via GH_PAT)
├── For each repository (5 parallel):
│   ├── Read .github/labels.yml (83 labels)
│   ├── Sync to repository
│   │   ├── Update existing labels
│   │   ├── Create missing labels
│   │   └── Keep extra labels (prune: false)
│   └── Report status
└── Generate summary report
```

## 🎓 Learn More

| Document | Purpose |
|----------|---------|
| [SETUP_CHECKLIST.md](.github/SETUP_CHECKLIST.md) | Complete setup verification |
| [workflows/SYNC_LABELS_SETUP.md](.github/workflows/SYNC_LABELS_SETUP.md) | Token setup details |
| [workflows/README.md](.github/workflows/README.md) | All workflow docs |
| [labels.yml](.github/labels.yml) | All 83 label definitions |
| [LABEL_SYNC_FIX.md](.github/LABEL_SYNC_FIX.md) | What was fixed and why |

## ⚠️ Important Notes

- **GH_PAT is required** for org-wide sync (without it, only current repo syncs)
- **Parent labels win**: Conflicts resolved in favor of `.github/labels.yml`
- **Child labels kept**: Extra labels in child repos are preserved
- **Runs weekly**: Automatic sync every Monday at 00:00 UTC
- **Safe testing**: Always test on single repo before full org sync

## 🆘 Need Help?

**Workflow not running?**
→ Check workflows are in `.github/workflows/` (not nested)
→ Push changes to register workflows with GitHub

**Permission errors?**
→ Verify `GH_PAT` secret exists
→ Check token has required permissions
→ See [SYNC_LABELS_SETUP.md](.github/workflows/SYNC_LABELS_SETUP.md)

**Labels not syncing?**
→ Verify workflow ran: `gh run list --workflow sync-labels.yml`
→ Check job logs for specific repo failures
→ Test single repo first for debugging

---

**Status**: ⚠️ Ready for token setup and first sync
**Action**: Create GH_PAT → Push changes → Run workflow
