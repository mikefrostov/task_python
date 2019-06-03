#!/bin/bash
set -e
freemem=$(free | grep Mem | awk '{print $4/$2 * 100.0}')
echo $freemem 
if [[ $freemem < 50 ]]
then
    reboot
fi 

