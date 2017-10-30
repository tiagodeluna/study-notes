# Git Commands

Git commands that I frequently use.

## Configuration

| Command | Description |
| ----- | ----- |
| git config --list | Display current configuration |
| git config --global `option` "value" | Set a global configuration |
| git config --local `option` "value" | Set a local (repository) configuration |
| git config `option` | Display the current value of a configuration entry. E.g: user.name, user.email |
| git config --global credential.helper "cache --timeout=3600" | Determine a interval in which it stores the user credentials for pulls and pushs |
| git remote add origin `repo` | Set a remote *repository* as the default origin |
| git remote set-url `branch` `repo` | Change the *repository* URL of a *branch* or *tag* |

**Setting merge and diff tool:**
In the .gitconfig file at <user folder>, add properties:
```
[merge]
     tool = meld
[mergetool "meld"]
     cmd = \"C:/Program Files (x86)/Meld/meld.exe\" $LOCAL $MERGED $REMOTE
[diff]
     tool = meld
[difftool "meld"]
     cmd = \"C:/Program Files (x86)/Meld/meld.exe\" $REMOTE $LOCAL
[mergetool]
     keepBackup = false
```

**Setting aliases to commands:**
Add aliases in the .gitconfig file at <user folder> as the following examples:
```
[alias]
     diff-meld = difftool --tool=meld -y 
     merge-meld = mergetool --tool=meld -y
```

## SSH Public Key

| Command | Description |
| ----- | ----- |
| ssh-keygen | Generate SSH Key |

## Cloning a project

| Command | Description |
| ----- | ----- |
| git clone `repo` | Clone a remote repository into a new local folder |

## Managing branches

| Command | Description |
| ----- | ----- |
| git branch `branch` | Create new *branch* |
| git branch `branch` -d | Delete a *branch* |
| git checkout -b `branch` `repo or branch` | Create local *branch* from a remote *repository* or *branch* and checkout it |
| git checkout -b `branch` `tag` | Create a new *branch* from a specific *tag* |

## Pulling files

| Command | Description |
| ----- | ----- |
| git pull `repo` `branch` | Pull files from remote *branch* of *repo*. If the branch is not informed, pull from *master* |
| git checkout --theirs . | Pull changes in branch, overwriting the local files when a conflict happens |
| git checkout --ours . | Pull changes in branch, maintaining local files when a conflict happens |

## Adding and Commiting

| Command | Description |
| ----- | ----- |
| git add `filename` | Add file |
| git add . -A | Add all untracked files in the working tree to the staging area |
| git add -u :/ | Update or remove previously tracked files from the entire working tree but not add new files |
| git commit -m `mensagem` | Perform a commit with a message associated |
| git commit --amend | Edit the last commit to include new added files and/or change the commit message |

## Pushing changes remotely

| Command | Description |
| ----- | ----- |
| git push `repo` `branch` | Send commited changes to a remove *branch* of a *repository* |
| git push --set-upstream `repo` `newbranch` | Push the current local branch and set the remote *newbranch* as upstream |

## Merging files

This is a three-step operation:

| Step | Command | Description |
| ----- | ----- | ----- |
| 1 | git checkout `branch` | Change to *branch* that will be updated. In case of code promotion, it is *master* |
| 2 | git merge `repo or branch` | Perform merge with the remote *branch* containing the changes |
| 3 | git push `repo` `branch` | Push changes to remote *branch* |

In case of conflicts after step 2, you'll need to perform the merge manually:

| Command | Description |
| ----- | ----- |
| git mergetool | Open the configured merge tool. Obs: use `:wq` to confirm the defult message in a automatic merge |

## Reverting changes

| Command | Description |
| ----- | ----- |
| git fetch \\\\ git reset --hard `repo or branch` | Fetch from the default remote (origin) \\\\ Reset your current branch to remote branch |
| git reset HEAD~`number` | Reset a *number* of commits (but it doesn't delete the commits, they still continue to exist) |
| git reset HEAD `filename` | Remove a *file* from the staging area |
| git checkout -- `filename` | Discard changes in a *file* in working directory |
| git merge --abort | Undo a merge, reverting the branch to its previous situation (usually after a merge the generated conflicts) |
	
# Using tags

| Command | Description |
| ----- | ----- |
| git tag | List the existing tags by alphabetical order |
| git tag `tagname` | Create a simple *tag* |
| git tag -a `tagname` -m `message` | Create an annotated, complete *tag* |
