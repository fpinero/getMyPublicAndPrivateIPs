#!/usr/bin/env python3

import requests
import socket
import subprocess

def get_ip():
    # Obtener IP privada
    try:
        local = subprocess.getoutput("ifconfig | grep 'inet ' | grep -Fv 127.0.0.1 | awk '{print $2}'")
    except:
        local = 'unknown'
    
    # Obtener IP pública
    try:
        public = requests.get('http://checkip.amazonaws.com').text.strip()
    except:
        public = 'unknown'
    
    return (local, public)

local_ip, public_ip = get_ip()
print(f"IP privada: {local_ip}")
print(f"IP pública: {public_ip}")

