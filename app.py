"""App"""
from datetime import datetime
from data import getLocation
from scanner import Scanner

now = datetime.now()
date = now.strftime("%m/%d/%Y")
time = now.strftime("%H:%M:%S")

scan = Scanner(getLocation())

print(f'Data: {scan.startScanner()}')
