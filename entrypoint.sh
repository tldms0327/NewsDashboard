#!/bin/bash

redis-server --port 6379 --daemonize yes

sleep 3

python3 crawling.py