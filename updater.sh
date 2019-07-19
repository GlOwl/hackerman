#!/bin/bash
(git fetch && git reset --hard && git pull) >> /var/log/hackerman.log 2> /var/log/hackerman.error
chmod +x updater.sh
