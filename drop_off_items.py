"Drop off items"
import time as t
from functions import getAgent

# TODO: Get agent
# TODO: Ask if items were dropped off successfully
# TODO: Add options
# TODO: Yes - for each item in pending list - remove from list - add to log
# TODO: No - "please contact HQ for futher steps" - quit
# TODO: quit

# Login
print('Login to start scanning.')
t.sleep(1)

agent, agentId = getAgent()
