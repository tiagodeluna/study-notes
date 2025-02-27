# UNIX COMMANDS

## DIRECTORIES AND FILES

| Command | Description |
| ----- | ----- |
| ls -al | Displays a directory content with extended info, including hidden files. |
| ls -sh <filename> | Displays the size of a given file. The -s is for "size", the -h is for "human readable". |
| cp -r <origin> <destiny> | Copies files or directories. Use -r for recursive copy. |
| mv <origin> <destiny> | Moves files or directories. It also can rename a directory from <origin> to <destiny>, if it doesn't yet exist. |
| rm -rf <foldername> | Remove folder. -r: recursive, -f: force. |
| tar xzf <file> | Extracts a tar.gz file |

---

## CONFIGURATION

| Command | Description |
| ----- | ----- |
| lsb_release -a | Displays the linux detailed distribution/release |
| df -h | Displays the amount of free disk space |
| export <VARIABLE>=<location> | Sets an environment variable. |
| set | Displays the environment variables and their functions. |
| printenv | The same as above command. |
| set grep '<user>' | Displays environment variables of an especific user. |
| echo $<variable name> | Displays the value of an especific variable. |
| printenv|grep <variable name> | The same as above command. |
| source ~/.bashrc | Executes the content of the file passed as argument (in this case, .bashrc), in the current shell. |

---

## PACKAGE ADMINISTRATION

| Command | Description |
| ----- | ----- |
| apt-add-repository <repository name> | Adds an external APT repository or removes an already existing repository. You must install the **software-properties-common** package to use this command. Find more information [here](http://manpages.ubuntu.com/manpages/xenial/man1/add-apt-repository.1.html) |
| apt-get install <package name> | Installs a new package. |
| apt-get -s install <package name> | Simulates installing the package, showing you what packages will be installed and configured. |
| apt-get update | Updates the package list. Run this command periodically to make sure your source list is up-to-date. |
| apt-get upgrade | Upgrades all installed packages |
| apt-get check | This command is a diagnostic tool. It does an update of the package lists and checks for broken dependencies. |
| apt-get -f install | This command fix broken packages. Do this if you get complaints about packages with "unmet dependencies". |
| apt-get autoclean | Removes .deb files for packages that are no longer installed on your system, in order to liberate diskspace. |
| apt-get remove <package_name> | Removes an installed package, leaving configuration files intact. |
| apt-get purge <package_name> | Completely removes a package and the associated configuration files. |
| update-alternatives --config <link group> | It updates the links in /etc/alternatives to point to the program for this purpose. It will list all of the choices for the link group of which given name is the master link. You will then be prompted for which of the choices to use for the link group. |
| dpkg -i <package name> | Queries, installs, removes, and maintains **Debian software packages** and their dependencies. This command, specifically, installs a Debian package. Find more information [here](https://www.computerhope.com/unix/dpkg.htm) |

---

## STATUS

| Command | Description |
| ----- | ----- |
| jps | Shows JVM processes status. |

---

## SERVICES

| Command | Description |
| ----- | ----- |
| systemctl [start|stop|restart|status|kill] <service name> | Manage services in a Linux distribution that supports systemd |
| service <service name> [start|stop] | Manage services installed using init.d |

