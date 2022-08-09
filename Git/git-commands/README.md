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

Check out [this article](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) to find more info on how to generate and use SSH keys in GitHub.

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
| git branch --unset-upstream | Detach/unset/remove remote branch (upstream) currently associated with the local branch |
| git fetch | Downloads references to all the remote branches and/or tags. |
| git checkout -b `branch` `repo, branch or tag` | Switch branches. With `-b` it creates a local *branch* from a remote *branch* or *tag* and switch to it |

## Pulling files

| Command | Description |
| ----- | ----- |
| git pull `repo` `branch` | Pull files from remote *branch* of *repo*. If the branch is not informed, pull from *master* |
| git checkout --theirs . | Pull changes in branch, overwriting the local files when a conflict happens |
| git checkout --ours . | Pull changes in branch, maintaining local files when a conflict happens |

## Reviewing, Adding and Commiting

| Command | Description |
| ----- | ----- |
| git log [--oneline] [--author="<username>"] | Display the commit history. Use `--oneline` to see just commit messages. Use `--author` to filter by user. |
| git diff [--cached] `filename` | See the differences between local and remote branches. Use `--cached` to see a file already in the staging area |
| git add `filename` | Add file |
| git add . -A | Add all untracked files in the working tree to the staging area |
| git add -u :/ | Update or remove previously tracked files from the entire working tree but not add new files |
| git commit -m `mensagem` | Perform a commit with a message associated |
| git commit -am `mensagem` | Add anything that was changed and commit with a message |
| git commit --amend [--no-edit] | Edit the last commit to include new added files and/or change the commit message. The `--no-edit` option allows to add staged changes to previous commit without changing commit message. |

## Pushing changes

| Command | Description |
| ----- | ----- |
| git push `repo` `branch` | Send commited changes to a remote *branch* of a *repository* |
| git push --set-upstream `repo` `newbranch` | Push the current local branch and set the remote *newbranch* as upstream |
| git push --force-with-lease | Overwrites a remote branch with your local branch, unless there are more commits added to the remote branch (f.e. by another team-member). `--force`is a more brute approach, because it ignores other commits in the remote. |

## Merging Branches and Solving Conflicts

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
| git fetch \\\\ git reset --hard [`branch`] | Fetch updated info from the remote (origin) \\\\ Reset local branch to its original state (default) or to another remote *branch* (if provided) |
| git reset HEAD~`number` | Reset a *number* of commits (but it doesn't delete the commits, they still continue to exist) |
| git reset HEAD `filename` | Remove a *file* from the staging area |
| git restore --staged `filename` | Similar to the one above,  remove a *file* from the staging area |
| git update-index --assume-unchanged `file` | Forces git to ignore local changes in a file by setting its state to "unchanged" |
| git merge --abort | Undo a merge, reverting the branch to its previous situation (usually after a merge the generated conflicts) |

## Untracking/Removing files

If you need to remove all items from the Git index (not from the working directory or local repository), and then update the Git index, you can use the series of commands below (f.e. in case you updated your `.gitignore` file and want to exclude the undesirable files from your repo).

| Step | Command | Description |
| ----- | ----- | ----- |
| 1 | git rm -r --cached . | Remove all files from the Git index (or cache) |
| 2 | git add . | Add all files again, respecting the new .gitignore definitions |
| 3 | git commit -m "Remove ignored files" | Commit the changes |

An alternative when you need a fresh start is the `git clean` command, as it excludes each and every file in your git directory which is NOT part of your repository. Usually it is used in conjunction with `git reset --hard` (see **Reverting changes** section above).

| Command | Description |
| ----- | ----- |
| git clean -Xdf -e <exclude_pattern> | Erases all the files in your git directory that are NOT part of your repo. The `-e` option allows you to ignore files from the "exclusion list" based on the given pattern (f.e. `git clean -Xdf -e \!.idea/\*\*`) |
	
## Using tags

| Command | Description |
| ----- | ----- |
| git fetch --tags | Fetch tags from remote repository |
| git tag -l `pattern`| `git tag` lists existing tags (on your local). By adding `-l` option you get all tags that match the pattern (e.g. `git tag -l "V1_*"`) |
| git tag `tagname` | Create a simple *tag* |
| git tag -a `tagname` -m `message` | Create an annotated, complete *tag* |
| git checkout tags/`tagname` -b `branch`| Checkout the given tagname and the branch to be checked out |

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

### Squashing commits

1. git log *//To see which commits you want to combine*
2. git rebase -i `multiple_options` *//This command will perform a rebase in Interactive Mode (`-i`). Basically, you have two options here: (1) Inform the SHA1 hash of the last commit you want to keep intact, so the rebase will select all commits after that one to combine (f.e. `git rebase -i 4e476d1e10d2`); (2) Inform the number of commits behind the current HEAD that you want to select (f.e. `git rebase -i HEAD~5`)*
3. An editor will open with the list of selected commits in chronological order (ignoring merge commits). You can reorder, remove or adjust them as you wish. There are several actions available such as 'pick', 'squash', 'edit', etc. To squash them in one single commit, keep the first line as 'pick', and change the consecutive lines to 'squash'. Salve and exit.
4. Enter a commit message for the new, combining commit. Save and exit.
5. git push

## Working with submodules

Submodules allow you to keep a Git repository as a subdirectory of another Git repository. This lets you clone another repository into your project and keep your commits separate. More information can be found [here](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

| Command | Description |
| ----- | ----- |
| git submodule add `repo url` `folder name` | Add a remote repo as a submodule in the current repo |
| git submodule update --init --recursive | Tells git to download the contents of submodule when downloading current repository |
