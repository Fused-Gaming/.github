# Workspace Setup Guide

This document explains the VS Code workspace configuration for the Fused Gaming organization repository.

## Overview

The workspace has been configured to optimize project coordination and documentation management for the Fused Gaming organization.

## Workspace Features

### 1. Editor Configuration

- **Auto-save**: Enabled on focus change
- **Format on save**: Automatically formats files when saved
- **Word wrap**: Enabled for better readability
- **Trailing whitespace**: Automatically trimmed
- **Final newline**: Automatically inserted

### 2. File Type Settings

#### Markdown (`.md`)
- Enhanced preview with GitHub flavoring
- Smart suggestions enabled
- Automatic formatting with Prettier
- Line length guide at 120 characters

#### YAML (`.yml`, `.yaml`)
- 2-space indentation
- Auto-formatting for GitHub workflows
- Syntax validation

#### JSON
- 2-space indentation
- Auto-formatting
- Schema validation

### 3. Recommended Extensions

The workspace recommends these extensions for installation:

#### Essential
- **EditorConfig**: Maintains consistent coding styles
- **Prettier**: Code formatter
- **Markdown All in One**: Markdown editing tools
- **MarkdownLint**: Markdown linting
- **GitHub Markdown Preview**: Enhanced preview

#### GitHub Integration
- **GitHub Actions**: Workflow support
- **GitHub Pull Requests**: PR management
- **GitLens**: Enhanced Git capabilities

#### Productivity
- **Todo Tree**: Tracks TODO comments
- **Better Comments**: Color-coded comments
- **Code Spell Checker**: Catches typos

#### Language Support
- **YAML**: YAML language support
- **JSON Language Service**: Enhanced JSON editing

### 4. Tasks

Access tasks via `Terminal > Run Task` or `Ctrl+Shift+P` > "Tasks: Run Task":

- **Validate YAML Files**: Lists all YAML files
- **List All Markdown Files**: Shows all documentation
- **List GitHub Issue Templates**: Shows available templates
- **Show Directory Structure**: Displays folder hierarchy

### 5. GitHub Issues Integration

Pre-configured queries for quick access:
- My Issues
- Created Issues
- Recent Issues
- All Open Issues
- Bug Reports
- Feature Requests

### 6. Git Configuration

- Smart commits enabled
- Auto-fetch enabled
- Sync confirmations disabled for smoother workflow
- Issue creation triggers for TODO, FIXME, BUG, HACK

## Configuration Files

### `.editorconfig`
Ensures consistent formatting across different editors:
- UTF-8 encoding
- LF line endings
- Spaces for indentation
- Trim trailing whitespace
- Insert final newline

### `.prettierrc.json`
Code formatting rules:
- 120 character line width
- 2-space indentation
- LF line endings
- Language-specific overrides

### `.gitignore`
Excludes:
- OS-specific files
- IDE configurations (except shared ones)
- Temporary files
- Logs
- Environment variables
- Node modules
- Build outputs

## Usage Tips

### Working with Markdown
1. Use `Ctrl+Shift+V` to preview markdown
2. The preview updates automatically
3. Use TODO comments - they'll appear in the Todo Tree view
4. Spell checker highlights typos automatically

### Managing GitHub Items
1. Use GitHub Issues panel (left sidebar)
2. View and create issues directly in VS Code
3. Manage PRs from the Source Control panel
4. Review GitHub Actions status inline

### File Organization
1. Explorer sorts by type automatically
2. Git ignored files are hidden
3. 20px indent for better hierarchy visualization
4. No preview mode - files open directly for editing

### Tasks Workflow
1. Press `Ctrl+Shift+B` for quick task access
2. Use tasks to validate YAML before committing
3. Check markdown files before publishing
4. Review templates before creating issues

## Customization

### Personal Settings
Add personal overrides to your user settings, not the workspace file.

### Additional Extensions
Feel free to install additional extensions that suit your workflow.

### Task Customization
Edit `.vscode/tasks.json` to add custom tasks for your needs.

## Troubleshooting

### Extensions Not Loading
1. Reload the window: `Ctrl+Shift+P` > "Developer: Reload Window"
2. Check the Extensions view for installation status

### Formatting Not Working
1. Ensure Prettier is installed
2. Check that "Format on Save" is enabled
3. Verify file type associations

### Git Issues
1. Ensure you have Git installed
2. Check Git config: `git config --list`
3. Verify repository remote: `git remote -v`

## Best Practices

1. **Commit Often**: Use descriptive commit messages
2. **Use Templates**: Leverage issue templates for consistency
3. **Format Before Commit**: Let auto-format handle styling
4. **Document Changes**: Update relevant docs when changing structure
5. **Review Before Push**: Use GitLens to review changes

## Resources

- [VS Code Documentation](https://code.visualstudio.com/docs)
- [Markdown Guide](https://www.markdownguide.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [EditorConfig](https://editorconfig.org/)
- [Prettier](https://prettier.io/)

---

For issues or suggestions about the workspace configuration, please open an issue using the appropriate template.
