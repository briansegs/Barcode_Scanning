"""App"""
from data import getLocation
from scanner import Scanner

scan = Scanner(getLocation())

scan.startScanner()

for value in scan.getData().values():
    print("----    ----")
    for k, v in value.items():
        print(f'{k}: {v}')
