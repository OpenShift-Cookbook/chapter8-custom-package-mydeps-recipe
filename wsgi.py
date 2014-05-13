#!/usr/bin/python
import os,sys
sys.path.append(os.path.join(os.getenv("OPENSHIFT_REPO_DIR"), "mydeps"))  

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass

from myapp import app as application