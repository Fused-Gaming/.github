# Fused Gaming Organization Setup Checklist

This checklist ensures the organization repository is properly configured for label sync and project coordination.

## ✅ Completed Setup

### Repository Structure
- [x] Workflows moved to correct location (`.github/workflows/`)
- [x] Label definitions merged into single source (`.github/labels.yml`)
- [x] VS Code workspace configured
- [x] Documentation created

### Label Configuration
- [x] 83 labels defined in `.github/labels.yml`
- [x] All labels from `labels.json` merged
- [x] Labels organized by category
- [x] Descriptions and colors defined

### Workflow Files
- [x] `sync-labels.yml` - Organization-wide label sync
- [x] `add-to-project.yml` - Auto-add to project boards
- [x] `auto-label-issues.yml` - Smart issue labeling
- [x] `goal-alignment-check.yml` - Goal proposal validation
- [x] `play_tictactoe.yml` - Interactive community game
- [x] `quarterly-okr-tracker.yml` - OKR tracking

### Documentation
- [x] `LABEL_SYNC_FIX.md` - Fix summary and changes
- [x] `workflows/SYNC_LABELS_SETUP.md` - Token setup guide
- [x] `workflows/README.md` - Workflow documentation
- [x] Root `README.md` - Repository overview
- [x] `WORKSPACE_GUIDE.md` - VS Code setup guide

## ⚠️ Action Required

### 1. Create GitHub Personal Access Token (PAT)

**Priority**: HIGH - Required for organization-wide label sync

**Steps**:
1. Go to: https://github.com/settings/tokens?type=beta
2. Click "Generate new token"
3. Configure:
   - Name: `Label Sync Token`
   - Expiration: 90 days
   - Repository access: All repositories
   - Permissions:
     - Issues: Read and write ✓
     - Metadata: Read-only ✓
4. Generate and copy token

### 2. Add PAT to Repository Secrets

**Priority**: HIGH

**Steps**:
1. Go to: Repository Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `GH_PAT`
4. Value: Paste your PAT from step 1
5. Click "Add secret"

**Verify**: The `sync-labels.yml` workflow should now have org-wide access

### 3. Test Label Sync

**Priority**: HIGH - Verify everything works

**Option A - Test on Single Repo**:
```bash
# Replace with actual repo name
gh workflow run sync-labels.yml -f target_repo="Fused-Gaming/test-repo"
```

**Option B - Full Org Sync**:
```bash
gh workflow run sync-labels.yml
```

**What to check**:
- Workflow completes successfully
- Labels appear in target repository
- No permission errors
- Summary report shows success

### 4. Commit All Changes

**Priority**: HIGH - Preserve the setup

```bash
cd "K:\git\projects\Fused Gaming"

# Stage all changes
git add .github/ .vscode/ .editorconfig .prettierrc.json .gitignore README.md WORKSPACE_GUIDE.md

# Review changes
git status

# Commit
git commit -m "Setup: Configure organization-wide label sync and workspace

- Merge all labels into .github/labels.yml (83 labels total)
- Fix workflow location (.github/.github/workflows → .github/workflows)
- Update sync-labels.yml for org-wide sync with matrix strategy
- Add comprehensive documentation and setup guides
- Configure VS Code workspace for project management
- Add EditorConfig and Prettier for consistent formatting

Resolves label sync failures and establishes single source of truth."

# Push to GitHub
git push origin main
```

### 5. Enable Branch Protection (Optional but Recommended)

**Priority**: MEDIUM - Prevent accidental label changes

**Steps**:
1. Go to: Repository Settings → Branches
2. Add rule for `main` branch
3. Enable:
   - Require pull request reviews (1 approval)
   - Require status checks (if applicable)
   - Include administrators
4. For `.github/labels.yml` specifically:
   - Consider requiring 2 approvals for changes
   - Add CODEOWNERS file if needed

### 6. Schedule Regular Reviews

**Priority**: LOW - Ongoing maintenance

**Quarterly Tasks**:
- Review label usage across repositories
- Remove unused labels
- Consolidate similar labels
- Update color schemes if needed
- Rotate PAT token (every 90 days)

## 📋 Verification Checklist

After completing setup, verify:

- [ ] `GH_PAT` secret exists and is valid
- [ ] Workflow runs successfully: `gh run list --workflow sync-labels.yml`
- [ ] Labels sync to at least one test repository
- [ ] No permission errors in workflow logs
- [ ] All 83 labels defined in `.github/labels.yml`
- [ ] Workflows are in `.github/workflows/` (not nested)
- [ ] Documentation is accessible and accurate
- [ ] VS Code workspace opens correctly
- [ ] All changes committed and pushed to GitHub

## 🔍 Troubleshooting

### Workflow fails with "Resource not accessible"
→ `GH_PAT` secret not configured or lacks permissions
→ See `.github/workflows/SYNC_LABELS_SETUP.md`

### Labels not syncing to child repos
→ Verify workflow ran successfully
→ Check individual job logs for specific repo failures
→ Ensure target repos exist and PAT has access

### Workflows not appearing in Actions tab
→ Workflows must be in `.github/workflows/` directory
→ Push changes to GitHub to register workflows
→ Wait a few minutes for GitHub to index

### Changes not taking effect
→ Ensure changes are committed and pushed
→ Workflow only runs on push to main branch
→ Manual trigger: `gh workflow run sync-labels.yml`

## 📚 Additional Resources

- [Label Definitions](/.github/labels.yml) - All 83 organization labels
- [Sync Setup Guide](/.github/workflows/SYNC_LABELS_SETUP.md) - Detailed token setup
- [Workflow README](/.github/workflows/README.md) - All workflow documentation
- [Workspace Guide](/WORKSPACE_GUIDE.md) - VS Code configuration
- [Fix Summary](/.github/LABEL_SYNC_FIX.md) - What was changed and why

## 🎯 Next Steps After Setup

1. **Announce Changes**: Notify team members about label standardization
2. **Update Documentation**: Link to label guide in project wikis
3. **Train Team**: Share `.github/LABELS_README.md` with contributors
4. **Monitor Usage**: Watch for label adoption across projects
5. **Iterate**: Adjust labels based on team feedback

---

**Setup Date**: 2026-01-12
**Status**: ⚠️ Pending GH_PAT configuration
**Next Action**: Create and add GH_PAT secret
