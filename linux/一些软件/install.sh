#!/bin/bash

# the script need run as root
if [ `id -u` -eq 0 ];then
    echo "root用户!"
else
    echo "非root用户!"
    exit 0
fi

add-apt-repository ppa:notepadqq-team/notepadqq

apt-get update

apt-get install notepadqq
