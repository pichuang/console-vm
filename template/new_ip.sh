#!/bin/bash
NEW_IP=$(vagrant ssh-config | grep HostName | awk '{print $2}')
echo "New IP Address:" $NEW_IP
sed -i "" "s/1.1.1.1/$NEW_IP/g" provisioning/hosts
#vagrant provision
