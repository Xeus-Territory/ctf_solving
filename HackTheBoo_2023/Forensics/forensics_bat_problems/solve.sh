#!/bin/bash

python3 batch_interpreter.py -f payload.bat| grep -oE '([A-Za-z0-9+/]+={0,2})' | tail -n 1 | base64 -d | tr -d '\0' | grep -oE 'HTB{[^}]*}'