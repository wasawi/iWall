#!/bin/bash

# Install brew:
#ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"

#update git
#brew install git

#install MC
#brew install mc

#install PV
#brew install pv

# Go to the path of this script
# http://stackoverflow.com/questions/4774054/reliable-way-for-a-bash-script-to-get-the-full-path-to-itself

pushd `dirname $0` > /dev/null
SCRIPTPATH=`pwd -P`

# Go back to your user path
# popd > /dev/null

#display current path
pwd

# Copy bash profile and aliases
#pv .bash_profile > ~/.bash_profile
#pv .alias.bash > ~/.alias.bash

#turn this script into an executable:
# http://stackoverflow.com/questions/19176973/how-to-execute-a-sequence-of-terminalubuntu-commands-without-pressing-the-retu


# Copy VLC preferences
pv vlcdc > ~/Library/Preferences/org.videolan.vlc/vlcrc
