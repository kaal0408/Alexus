import os 

class config(object):
   SUDO_ID = os.environ.get("SUDO_ID", "")
