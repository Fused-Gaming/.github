# Organization-Wide Label Sync Setup Guide

## Overview

The `sync-labels.yml` workflow syncs labels from [.github/labels.yml](../labels.yml) across **all repositories** in your organization.

## Token Requirements

### Option 1: GitHub Personal Access Token (Recommended for Org-Wide Sync)

For syncing across all organization repositories, you need a Personal Access Token (PAT) with organization-wide permissions.

#### Creating a PAT:

1. Go to GitHub Settings → Developer settings → Personal access tokens → Fine-grained tokens
2. Click "Generate new token"
3. Configure:
   - **Name**: `Label Sync Token`
   - **Expiration**: 90 days (or longer)
   - **Repository access**: All repositories
   - **Permissions**:
     - Repository permissions:
       - Issues: Read and write
       - Metadata: Read-only
     - Organization permissions (if applicable):
       - Members: Read-only (to list repos)

4. Click "Generate token" and copy it

#### Adding the PAT to your repository:

1. Go to your repository Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `GH_PAT`
4. Value: Paste your PAT
5. Click "Add secret"

### Option 2: Default GITHUB_TOKEN (Limited Scope)

If you don't create a `GH_PAT` secret, the workflow will fall back to using the default `GITHUB_TOKEN`. However, this has limitations:

- ⚠️ Can only sync labels to the **current repository**
- ❌ Cannot access other repositories in the organization
- ✅ No setup required
- ✅ Automatically available

**Recommendation**: Use Option 1 (GH_PAT) for true organization-wide sync.

## Workflow Features

### 1. Automatic Sync Modes

The workflow runs in three scenarios:

#### Weekly Schedule
- Runs every Monday at 00:00 UTC
- Syncs to all organization repositories
- Completely automated

#### On Push
- Triggers when you push changes to:
  - `.github/labels.yml`
  - `.github/workflows/sync-labels.yml`
- Ensures labels stay in sync immediately after changes

#### Manual Trigger
- Run via GitHub Actions UI
- Optional: Sync to a single repository
- Useful for testing or one-off syncs

### 2. Sync Behavior

- **Source**: `.github/labels.yml` (83 labels)
- **Targets**: All repositories in the organization
- **Conflict Resolution**: Parent labels override child labels
- **Prune Mode**: Disabled (child repos can have extra labels)
- **Parallel Processing**: Syncs up to 5 repos at once
- **Failure Handling**: Continues even if one repo fails

## Usage

### Sync All Repositories (Recommended)

```bash
# Via GitHub CLI
gh workflow run sync-labels.yml

# Or via GitHub UI
# Actions → Sync Organization Labels → Run workflow → Run workflow
```

### Sync Single Repository (Testing)

```bash
# Via GitHub CLI
gh workflow run sync-labels.yml -f target_repo="Fused-Gaming/your-repo-name"

# Or via GitHub UI
# Actions → Sync Organization Labels → Run workflow
# Enter repository name in "Target repository" field
# Click "Run workflow"
```

### Sync After Label Changes

```bash
# Just push your changes - workflow auto-runs
git add .github/labels.yml
git commit -m "Update organization labels"
git push
```

## Monitoring

### Check Workflow Status

```bash
# Via GitHub CLI
gh run list --workflow sync-labels.yml

# View specific run
gh run view <run-id>

# Watch live run
gh run watch
```

### View Sync Summary

After each run, check the workflow summary:
1. Go to Actions → Sync Organization Labels
2. Click on the latest run
3. View the summary showing:
   - Success/failure for each repository
   - Timestamp
   - Number of labels synced

## Troubleshooting

### Error: "Resource not accessible by integration"

**Cause**: Default `GITHUB_TOKEN` doesn't have org-wide permissions

**Solution**: Create and add a `GH_PAT` secret (see Option 1 above)

### Error: "404 Not Found" for a repository

**Causes**:
- Repository is private and token lacks access
- Repository was renamed or deleted
- Token permissions are insufficient

**Solutions**:
- Verify repository exists: `gh repo view Fused-Gaming/repo-name`
- Check PAT has access to private repos
- Update PAT permissions if needed

### Labels not syncing

**Causes**:
- Workflow hasn't run yet
- Workflow failed silently
- Repository has protected labels

**Solutions**:
- Manually trigger workflow
- Check workflow runs in Actions tab
- Review repository settings for label restrictions

### Some repositories skipped

**Expected behavior**: The workflow uses `fail-fast: false`, meaning it continues even if one repository fails. Check individual job logs to see which repos succeeded/failed.

## Best Practices

### 1. Test First
Before syncing to all repos, test on a single repository:
```bash
gh workflow run sync-labels.yml -f target_repo="Fused-Gaming/test-repo"
```

### 2. Schedule Maintenance Window
For major label changes, consider:
- Temporarily disabling the schedule
- Running manual sync during low-activity periods
- Announcing changes to contributors

### 3. Monitor Initial Sync
Watch the first full sync closely:
```bash
gh run watch
```

### 4. Document Custom Labels
If child repositories need custom labels:
- Document them in the child repo's README
- Add comments explaining why they're needed
- Consider promoting common ones to the parent labels.yml

### 5. Review Regularly
- Quarterly review of label usage
- Remove unused labels from parent definition
- Consolidate similar labels

## Configuration Options

### Adjust Sync Frequency

Edit `.github/workflows/sync-labels.yml`:

```yaml
schedule:
  # Daily at 2 AM UTC
  - cron: '0 2 * * *'

  # Twice weekly (Monday and Thursday)
  - cron: '0 0 * * 1,4'

  # Monthly (1st of month)
  - cron: '0 0 1 * *'
```

### Change Parallel Processing

Edit the `max-parallel` setting:

```yaml
strategy:
  max-parallel: 10  # Increase for faster sync (default: 5)
  # Or: 1 for sequential processing
```

### Enable Prune Mode (Advanced)

⚠️ **Warning**: This removes labels from child repos that aren't in the parent definition.

Edit the sync step:

```yaml
- name: Sync labels to ${{ matrix.repository }}
  uses: micnncim/action-label-syncer@v1
  with:
    manifest: .github/labels.yml
    repository: ${{ matrix.repository }}
    prune: true  # Change from false to true
```

## Security Considerations

### Token Security
- Never commit tokens to the repository
- Use repository secrets for token storage
- Rotate tokens regularly (every 90 days recommended)
- Use fine-grained tokens with minimal permissions
- Audit token usage in GitHub settings

### Access Control
- Limit who can manually trigger workflows
- Review workflow runs regularly
- Enable branch protection for `.github/labels.yml`
- Require pull request reviews for label changes

### Monitoring
- Set up notifications for workflow failures
- Review sync logs periodically
- Watch for unauthorized label changes
- Track which labels are being used across repos

## Support

### Issues with this workflow?
1. Check workflow logs in the Actions tab
2. Verify token permissions
3. Test with a single repository first
4. Review error messages in job output

### Need to modify labels?
1. Edit `.github/labels.yml`
2. Commit and push
3. Workflow automatically syncs changes
4. Verify in a test repository first

### Questions about label strategy?
- Review [../LABELS_README.md](../LABELS_README.md)
- Check [../LABEL_SYNC_FIX.md](../LABEL_SYNC_FIX.md) for context

---

**Last Updated**: 2026-01-12
**Workflow Version**: 2.0 (Organization-wide sync)
**Total Labels**: 83
