# Branch Protection Configuration

This directory contains files to help protect the main branch of the repository.

## Files

### CODEOWNERS
- Requires approval from @ftruter for all changes to any file in the repository
- This ensures that only the repository owner can approve changes

### workflows/branch-protection.yml
- GitHub Actions workflow that validates PR authors before merging to main
- Automatically fails if someone other than @ftruter tries to create a PR to main

## Additional Steps Required

To fully protect the main branch, you need to enable branch protection rules in GitHub:

1. Go to your repository on GitHub
2. Click on **Settings** → **Branches**
3. Under "Branch protection rules", click **Add rule**
4. Configure the following settings:
   - **Branch name pattern**: `main`
   - ✅ **Require a pull request before merging**
     - ✅ **Require approvals** (set to 1)
     - ✅ **Dismiss stale pull request approvals when new commits are pushed**
   - ✅ **Require status checks to pass before merging**
     - Add the `enforce-branch-protection` check
   - ✅ **Require conversation resolution before merging**
   - ✅ **Include administrators** (this applies rules to you as well, but you can still bypass)
   - ✅ **Restrict who can push to matching branches**
     - Add only your username: `ftruter`
   - ✅ **Do not allow force pushes** (disable for maximum protection)
   - ✅ **Do not allow deletions**

5. Click **Create** or **Save changes**

## How It Works

With these configurations in place:
1. **CODEOWNERS** ensures you must approve all changes
2. **Branch protection workflow** prevents unauthorized PRs from being merged
3. **GitHub branch protection rules** (once configured) prevent direct pushes to main by anyone except you

This creates a multi-layered protection system for the main branch.
