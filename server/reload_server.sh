#!/bin/sh
echo "Pulling from master..."
git pull origin master
echo "Successfully pulled from master!"
echo "Restarting server..."
kill -HUP `cat main.pid`
