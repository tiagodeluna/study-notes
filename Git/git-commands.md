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
| git add . -A | Add all untracked files to the Staging Area |
| git add -u :/ | Update or remove previously tracked files but not add new files |
