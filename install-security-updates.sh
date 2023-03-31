#!/bin/bash
# Script to download security updates on Debian-based OSes

# update package lists
sudo apt-get update

# create config file to get security updates when you run "apt-get upgrade" (more info here: https://askubuntu.com/a/272)
echo 'Package: *
Pin: release a=lucid-security
Pin-Priority: 500

Package: *
Pin: release o=Ubuntu
Pin-Priority: 50' > apt-upgrade.conf.tmp

# install the security updates
sudo apt-get -o Dir::Etc::Preferences=./apt-upgrade.conf.tmp upgrade -y

# delete the temporary config files
rm ./apt-upgrade.conf.tmp

# check for security updates that may have been missed by the previous method
sudo apt-get -s dist-upgrade | grep "^Inst" |
    grep -i securi | awk -F " " {'print $2'} |
    xargs apt-get install -y

# finally, just to ensure that nothing was missed before
sudo apt list --upgradable | grep security |cut -d\/ -f1|xargs sudo apt-get install -y
