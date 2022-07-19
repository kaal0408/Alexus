import os 

#----Sudo Configuration----#
SUDO_ID = os.environ.get("SUDO_ID", "")
DURATION_LIMIT = os.environ.get("DURATION_LIMIT", 100)
COMMAND_PREFIXES = (os.environ.get("COMMAND_PREFIXES", "/ !").split()
que = {}

