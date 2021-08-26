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

### Setting merge and diff tool:
In the .gitconfig file at `user folder`, add properties:
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

### Setting aliases to commands:
Add aliases in the .gitconfig file at `user folder` as the following examples:
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
| git clone `repo` [`folder name`] | Clone a remote repository into a new local folder |
| git clone `repo` \\\\ git reset --hard `SHA1` | Clone a specific commit |

## Managing branches

| Command | Description |
| ----- | ----- |
| git branch [-r] | Display all local or remote (with `-r`) existing branches. |
| git branch `branch` | Create new *branch* |
| git branch `branch` -d | Delete a *branch* |
| git checkout -b `branch` `repo, branch or tag` | Create local *branch* from a remote *repository*, *branch* or *tag* and switch (checkout) to it |

## Pulling files

| Command | Description |
| ----- | ----- |
| git pull `repo` `branch` | Pull files from remote *branch* of *repo*. If the branch is not informed, pull from *master* |
| git checkout --theirs . | Pull changes in branch, overwriting the local files when a conflict happens |
| git checkout --ours . | Pull changes in branch, maintaining local files when a conflict happens |

## Reviewing, Adding and Commiting

| Command | Description |
| ----- | ----- |
| git log [--oneline] | Display the commit history. Use `--oneline` to see just commit messages. |
| git diff [--cached] `filename` | See the differences between local and remote branches. Use `--cached` to see a file already in the staging area |
| git add `filename` | Add file |
| git add . -A | Add all untracked files in the working tree to the staging area |
| git add -u :/ | Update or remove previously tracked files from the entire working tree but not add new files |
| git commit -m `mensagem` | Perform a commit with a message associated |
| git commit -am `mensagem` | Add anything that was changed and commit with a message |
| git commit --amend | Edit the last commit to include new added files and/or change the commit message |

## Pushing changes

| Command | Description |
| ----- | ----- |
| git push `repo` `branch` | Send commited changes to a remove *branch* of a *repository* |
| git push --set-upstream `repo` `newbranch` | Push the current local branch and set the remote *newbranch* as upstream |

## Merging Branches ans Solving Conflicts

This is a three-step operation:

| Step | Command | Description |
| ----- | ----- | ----- |
| 1 | git checkout `branch` | Change to *branch* that will be updated. In case of code promotion, it is *master* |
| 2 | git merge `repo or branch` | Perform merge with the remote *branch* containing the changes |
| 3 | git push `repo` `branch` | Push changes to remote *branch* |

In case of conflicts after step 2, you'll need to perform the merge manually:

| Command | Description |
| ----- | ----- |
| git log -p `file` | Displays the change history of a file in text format |
| gitk `file` | Displays the commit history of a file in a graphic interface. If no file is specified, it shows the history of the merge |
| git mergetool | Open the configured merge tool. Obs: use `:wq` to confirm the defult message in an automatic merge |

## Reverting changes

| Command | Description |
| ----- | ----- |
| git reset --hard | Reset the local branch to its original state |
| git fetch \\\\ git reset --hard `repo or branch` | Fetch from the default remote (origin) \\\\ Reset your current branch to remote branch |
| git reset HEAD~`number` | Reset a *number* of commits (but it doesn't delete the commits, they still continue to exist) |
| git reset HEAD `filename` | Remove a *file* from the staging area |
| git checkout -- `filename` | Discard changes in a *file* in working directory |
| git merge --abort | Undo a merge, reverting the branch to its previous situation (usually after a merge the generated conflicts) |
| git update-index --assume-unchanged `file` | Forces git to ignore local changes in a file by setting its state to "unchanged" |

## Untracking/Removing files

If you need to remove all items from the Git index (not from the working directory or local repository), and then update the Git index, you can use the series of commands below (f.e. in case you updated your `.gitignore` file and want to exclude the undesirable files from your repo).

| Step | Command | Description |
| ----- | ----- | ----- |
| 1 | git rm -r --cached . | Remove all files from the Git index (or cache) |
| 2 | git add . | Add all files again, respecting the new .gitignore definitions |
| 3 | git commit -m "Remove ignored files" | Commit the changes |
	
## Using tags

| Command | Description |
| ----- | ----- |
| git tag | List the existing tags by alphabetical order |
| git tag `tagname` | Create a simple *tag* |
| git tag -a `tagname` -m `message` | Create an annotated, complete *tag* |

## Integrating branches/commits

### Merging branches

1. git checkout `target branch`
2. git merge `source branch`
   1. git diff `filename` *//Just in case of conflicts occurring, to check it*
   2. git mergetool *//Just in case of conflicts occurring, to resolve them*
   3. git commit *//idem*
3. git push

### Cherry picking commits

1. git checkout `target branch`
2. git cherry-pick `one or more commit hashes` *//This will copy the commits of another branch and add them as new commits on the target branch*
   + *If the cherry picking gets halted because of conflicts, resolve them (see step 2 on Merging Branches above) and...*
      - git cherry-pick --continue *//if you want to finish the process, OR*
      - git cherry-pick --abort *//if you want to abort the process*
3. git push

## Working with submodules

| Command | Description |
| ----- | ----- |
| git submodule add `repo url` `folder name` | Add a remote repo as a submodule in the current repo |
| git submodule update --init --recursive | Tells git to download the contents of submodule when downloading current repository |
