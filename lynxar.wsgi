#!/usr/bin/python
import sys
import logging
from env import root

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,root)

from lynxarAPI import app as application
application.secret_key = ''
