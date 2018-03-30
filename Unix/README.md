# UNIX COMMANDS

## DIRECTORIES AND FILES

| Command | Description |
| ----- | ----- |
| ls -al | Displays a directory content with extended info, including hidden files. |
| cp <origin> <destiny> | Copies files or directories. |
| mv <origin> <destiny> | Moves files or directories. It also can rename a directory from <origin> to <destiny>, if it doesn't yet exist. |
| rm -rf <foldername> | Remove folder |
| tar xzf <file> | Extracts a tar.gz file |
| nano <file> | Edits file with 'Nano' editor. |
| vi <file> | Edits file with 'Vi' editor. |

---

## CONFIGURATION

| Command | Description |
| ----- | ----- |
| lsb_release -a | Displays the linux detailed distribution/release |
| df -h | Displays the amount of free disk space |
| export <VARIABLE>=<location> | Sets an environment variable. |
| set | Displays the environment variables and their functions. |
| set grep '<user>' | Displays environment variables of an especific user. |
| source ~/.bashrc | Applies changes in the environment variables file (in this case, .bashrc). |
| echo <variable name> | Displays the value of an especific variable. |

---

## PACKAGE ADMINISTRATION

| Command | Description |
| ----- | ----- |
| apt-get install <package name> | Installs a new package. |
| apt-get -s install <package name> | Simulates installing the package, showing you what packages will be installed and configured. |
| apt-get update | Run this command periodically to make sure your source list is up-to-date. |
| apt-get upgrade | Upgrades all installed packages |
| apt-get check | This command is a diagnostic tool. It does an update of the package lists and checks for broken dependencies. |
| apt-get -f install | This command fix broken packages. Do this if you get complaints about packages with "unmet dependencies". |
| apt-get autoclean | Removes .deb files for packages that are no longer installed on your system, in order to liberate diskspace. |
| apt-get remove <package_name> | Removes an installed package, leaving configuration files intact. |
| apt-get purge <package_name> | Completely removes a package and the associated configuration files |

## STATUS

| Command | Description |
| ----- | ----- |
| jps | Shows JVM processes status. |
