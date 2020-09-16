#!/bin/bash
echo "Pulling from master..."
git pull origin master
echo "Successfully pulled from master!"
echo "Installing new dependencies"
source venv/bin/activate
pip3 install -r requirements.txt
echo "Restarting server..."
kill -HUP `cat main.pid`
