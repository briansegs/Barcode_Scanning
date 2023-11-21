"""App"""
from data import getLocation
from scanner import Scanner

# TODO: get mock data from database {invetory}
# TODO: check if scanned data is in inventory
# TODO: add scanned data to database

scan = Scanner(getLocation())

scan.startScanner()

for value in scan.getData().values():
    print("----    ----")
    for k, v in value.items():
        print(f'{k}: {v}')
