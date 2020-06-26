#!/usr/bin/python
import sys
import logging
import env

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,env.root())

from lynxarAPI import app as application
application.secret_key = ''
