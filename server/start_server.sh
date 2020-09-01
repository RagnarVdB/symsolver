#!/bin/bash
cd ~/Documents/sympy-GUI/server
source venv/bin/activate
gunicorn main:app -w 9 -p main.pid -D
