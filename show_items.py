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
