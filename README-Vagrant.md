# Vagrant Setup: 

Step 1: Open the GitBash/Cmder. 

Step 2: Clone the mentioned Vagrant Git Repo: 
```
 git clone https://github.com/amitvashisttech/vagrant-setup.git
```

Step 3: Change the Directory to DevOps: 
```
$ cd vagrant-setup/devops/
```

Step 4: Run Vagrant in order to setup required virtual machines: 
```
$ vagrant.exe up
Bringing machine 'master' up with 'virtualbox' provider...
Bringing machine 'worker1' up with 'virtualbox' provider...
Bringing machine 'worker2' up with 'virtualbox' provider...
==> master: Importing base box 'ubuntu/xenial64'...
==> master: Matching MAC address for NAT networking...
==> master: Checking if box 'ubuntu/xenial64' version '20191211.0.0' is up to date...
```

Step 5: Check VM Status:
```
$ vagrant.exe status
Current machine states:
master running (virtualbox)
worker1 running (virtualbox)
worker2 running (virtualbox)
This environment represents multiple VMs. The VMs are all listed above with their current state. 
```

Step 6: Login to VM:
```
$ vagrant.exe ssh master
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-170-generic x86_64)
* Documentation: https://help.ubuntu.com
* Management: https://landscape.canonical.com
* Support: https://ubuntu.com/advantage
59 packages can be updated.
41 updates are security updates.
New release '18.04.4 LTS' available.
Run 'do-release-upgrade' to upgrade to it.
vagrant@master:~$
```

Step 7: In order to poweroff & destroy VM:
```
$ vagrant.exe halt master
```
```
$ vagrant.exe status
Current machine states:
master poweroff (virtualbox)
worker1 poweroff (virtualbox)
worker2 poweroff (virtualbox)
This environment represents multiple VMs. The VMs are all listed
above with their current state. For more information about a specific
VM, run `vagrant status NAME`.
```

Destroy:
```
$ vagrant.exe destroy master
 master: Are you sure you want to destroy the 'master' VM? [y/N] y
```


