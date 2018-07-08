# Vagrant VM Managing

## Creation Steps (example)

1. Create VM config file
   * `vagrant init --minimal ubuntu/xenial64`
2. Get Box Package (from a source outside of the Vagrant Cloud, if needed)
   * `vagrant box add ubuntu/xenial64 https://app.vagrantup.com/ubuntu/boxes/xenial64/versions/20180126.0.0/providers/virtualbox.box`
3. Boot the VM
   * `vagrant up`
4. Shell into it
   * `vagrant ssh`

## Commands

| Command | Effect |
| ----- | ----- |
| vagrant up | Boot a stopped VM or resume a suspended one. |
| vagrant ssh | Shell into the VM. |
| vagrant ssh-config | Return useful SSH info, including the IP and SSH port to use. |
| vagrant halt | Shut down the running. |
| vagrant suspend | Suspend the VM, saving its state. |
| vagrant resume | Resume a previously suspended VM. |
| vagrant reload --provision | Reload VM - to apply changes made to Vagrantfile, for example. |
| vagrant destroy | Stop the running VM and destroy all resources created during the machine creation process. |
| vagrant box list | List all base boxes already installed in your computer. These base boxes live in your `%userprofile%/.vagrant.d/boxes` folder. |
| vagrant box remove `box/name` | Delete boxes installed in your machine. |