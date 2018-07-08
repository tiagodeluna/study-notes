# Vagrant VM Managing


## Creation Steps

1. Create VM config file
   * `vagrant init --minimal ubuntu/xenial64`
2. Get Box Package
   * `vagrant box add ubuntu/xenial64 https://app.vagrantup.com/ubuntu/boxes/xenial64/versions/20180126.0.0/providers/virtualbox.box`
3. Boot the VM
   * `vagrant up`
4. Shell into it
   * `vagrant ssh`


## Commands

| Command | Effect |
| ----- | ----- |
| vagrant up | Boot the VM |
| vagrant ssh | Shell into the VM |
| vagrant halt | Shut down the running VM |
| vagrant suspend | Suspend the VM, saving its state |
| vagrant resume | Resumes a previously suspended VM |
| vagrant reload --provision | Reload VM - to apply changes made to Vagrantfile, for example |
| vagrant destroy | Stop the running VM and destroy all resources created during the machine creation process |