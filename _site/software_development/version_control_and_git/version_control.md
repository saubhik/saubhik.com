## Version Control
Suppose we are making a development project. A VCS, version control system, makes us able to
* revert back changes in case we need to go back in time
* keeps track of contributions from different coders, to different files

**Repository**: Simply a fancy name for a project directory.

**Centralised VCS**: Uses a client-server model. There is one repository file system in a server.
Connect to the network server every time you work on the repository.

**Distributed VCS**: Peer-to-peer approach. All developers have their own copies of their files
and changes to the files are also saved locally.

In git, first you *modify* a file. Then you add it to the *staging area* where you review
the changes. Then you *commit* them to make the changes a part of development history.
Commits are uniquely identified by their SHAs.

Some common git commands:
```git
# Initialise git repository
git init
# Stage files
git add filename
# Commit files
git commit -m "commit message"
# Link remote repository to local repository
git remote add origin <url of remote repository>
# Push changes from local's master to remote's master
git push -u origin master
# Status - files modified and staged or not
git status
# Commit details in reverse chronological order
git log
```

In `git remote add`, `origin` is the remote repo name, and `url` is the remote repo url.
The `url` is a something which ends with `.git`.

How do we go back in time?
```git
# Get the commit IDs or SHAs
git log --oneline
# Go back to previous state of a file - discard unstaged & uncommited changes to filename
git checkout -- filename
# Make a new commit to revert the previous commit commit_id
git revert commit_id
# Make commit_id the latest commit and remove everything afterwards
git reset --hard commit_id
```

How do we clean staged changes?
```git
# Check the status of unwanted changes
git status
# Reset the buffer zone to HEAD
git reset HEAD filename
# Remove unwanted changes from working directory - switch to commit version
git checkout -- filename
```

Creating branches and parallelising development. A branch is a movable pointer in git that
points to a commit. HEAD pointer points to the commit to which the current branch pointer is 
pointing.
```git
# Create a branch
git branch branchname
# Show all branches and current working branch
git branch
# Move from one branch to another - HEAD pointer now points to branch
git checkout branch
# Merge branch branchname with current branch
git merge branchname
# Deleting branch branchname
git branch -d branchname
# Check differences between commits
git diff commit_1 commit_2
# Check diff between branches
git diff branchname_1..branchname_2
```

Forking is a GitHub-specific functionality. You can only `git clone` a remote repository
to create a local repo on your system.

For syncing with a remote repo either do a `git fetch` or a `git pull`. `git pull` does
a `git fetch` and a `git merge`.

Updating your fork in GitHub with remote repo:
```git
# Checkout to master
git checkout master
# Pull the needed branch from upstream repo
git pull upstream_repo_url branchname_in_upstream_repo
# If there are any conflicts, resolve them and make a git commit
# Next, push the merge commit to remote repo
git push origin master
```
