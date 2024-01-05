"Show items scanned"
import time as t
from functions import getAgent

# TODO: Login agent
# TODO: Show items scanned options:
# TODO: All dates earliest to latest
# TODO: All dates latest to earliest
# TODO: Pick from dates
# TODO: By agent
# TODO: By location
# TODO: Extract function for login

# Login
print("Login to continue. ")
t.sleep(1)

agent, agentId = getAgent()

print(f"Welcome {agent}.")
t.sleep(.5)

# Options
while True:
    print("Options")
    t.sleep(.5)
    print('''
    1. Show all dates earliest to latest
    2. Show all dates latest to earliest
    3. Show by date
    4. Show by agent
    5. Show by location
    ''')
    t.sleep(.5)
    opt = input(">>> ")
