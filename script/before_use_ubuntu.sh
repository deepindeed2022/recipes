#! /bin/bash
#
# installsubl.sh
# Copyright (C) 2016 charles <charles@ubuntuG>
#
# Distributed under terms of the MIT license.
#
for req in $(cat install_software.txt); do sudo apt-get install $req; done

# install sublime
wget https://download.sublimetext.com/sublime-text_build-3114_amd64.deb
sudo dpkg -i ~/Download/sublime-text_build-3114_amd64.deb
cd ~/Download
dpkg -i sublime-text_build-3114_amd64.deb

