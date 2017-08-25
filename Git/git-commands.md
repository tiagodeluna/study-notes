# Git Commands

## Configuration

| Command | Description |
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
