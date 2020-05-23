#!/bin/bash
VERSION=1.0
echo "Building Video Encryption Tool version "$VERSION
MY_PATH="`dirname \"$0\"`"              # relative
MY_PATH="`( cd \"$MY_PATH\" && pwd )`"  # absolutized and normalized
if [ -z "$MY_PATH" ] ; then
  # error; for some reason, the path is not accessible
  # to the script (e.g. permissions re-evaled after suid)
  exit 1  # fail
fi
#echo $MY_PATH
cd $MY_PATH/../
apt-get install python3 python3-pip
pip3 install -r requirements.txt
echo "Setup done Successfully!"
