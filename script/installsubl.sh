#! /bin/bash
#
# installsubl.sh
# Copyright (C) 2016 charles <charles@ubuntuG>
#
# Distributed under terms of the MIT license.
#



wget https://download.sublimetext.com/sublime-text_build-3114_amd64.deb
sudo dpkg -i ~/Download/sublime-text_build-3114_amd64.deb


# install from https://www.sublimetext.com/docs/3/linux_repositories.html
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
# echo "deb https://download.sublimetext.com/ apt/dev/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update
sudo apt-get install sublime-text
