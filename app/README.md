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

This will install all of the required packages listed in the `requirements.txt` file.
