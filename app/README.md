# Barcode Scanner

## Introduction

This project was created to help a friend test a business idea. He wanted to scan items, mark them for drop off, ship those items, and then drop them off at a storage facility. Items would be scanned at different locations around the East Coast of the United States and dropped off at one central location. This program is built around his specific needs but functions as a C.R.U.D. program. 

The program starts by logging in a user by scanning their unique barcode number. If they are not in the database as an agent they won't be able to continue. Next, the user is presented with a menu of options. They can scan items for pickup, drop off items, show a record of items scanned, show items pending drop off, and show a log of items that have been dropped off.

The application easily flows from different menus and options offering a pleasant user experience. Everything is stored on a local database for ease and speed. The program uses a laptop's camera to do the scanning. This was important for my client to pitch his idea. Over all, he was very happy with what I built for him and I had a good time building it.

## Dependencies
### Local Development

Make sure you have Python3 and pip installed.

#### Python 3.7

[python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

Instructions for setting up your virual enviornment:\
[Virtual Enviornment docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Setup virtual environment: 
```bash
python3 -m venv .venv
```

Run virtual environment:
```bash
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

This will install all of the required packages listed in the [requirements.txt](https://github.com/briansegs/Barcode_Scanning/blob/main/app/requirements.txt) file.

#### Key Dependencies

[Open CV](https://opencv.org/) is the world's biggest computer vision library.

[Pandas](https://pandas.pydata.org/) is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.

[Pyzbar](https://pypi.org/project/pyzbar/) Read one-dimensional barcodes and QR codes from Python 2 and 3 using the zbar library.

## Using the Application
#### Setting up the database
Change the database name (Or keep it the same) in the [data](https://github.com/briansegs/Barcode_Scanning/blob/f8604f37cac6d32549e59b683d283f7e9b494d62/app/data/data.py#L3) file.

#### Running the app
```bash
python3 main.py
```

## Managing the data
```bash
python3 manage_tables.py
```
[manage_tables.py](https://github.com/briansegs/Barcode_Scanning/blob/main/app/manage_tables.py) is A script that manages the database and helps with testing. 
