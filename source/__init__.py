#!/usr/bin/env python
# -*- coding: utf-8 -*-

# source/__init__.py

"""This module executes and defines what symbols the package exposes to the outside world."""

__author__ = "Rakesh Singh"
__copyright__ = "Copyright 2023, Project Magnetar"
__version__ = "1.0"
__maintainer__ = "Rakesh Singh"
__email__ = "support@datapatrons.com"
__status__ = "Production"


# Third party library
from flask import Flask


# Creating a variable which simply creates the application object as an instance of class Flask
# imported from the flask package. The dunder variable is set to the name of the module in which it is used
app = Flask(__name__)
# The bottom import of "routes" module is a workaround to circular imports, a common problem with Flask applications
from source import routes
