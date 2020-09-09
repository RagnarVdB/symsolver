#!/bin/sh
echo "Pulling from master..."
git pull origin master
echo "Successfully pulled from master!"
echo "Restarting server..."
source venv/bin/activate
pip3 install -r requirements.txt
kill -HUP `cat main.pid`
