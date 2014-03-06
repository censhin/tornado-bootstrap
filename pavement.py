#!/usr/bin/env python

import sys
from os.path import dirname, realpath

import paver.doctools
from paver.easy import options
from paver.setuputils import setup, find_packages

# make sure the current directory is in the python import path
sys.path.insert(0, dirname(realpath(__file__)))

# import our tasks
from tasks.tests import *
from tasks.virtualenv import *
from tasks.run_pep8 import *

#
# project dependencies
#

install_requires = [
    'setuptools',
    'cerberus',
    'mock',
    'pep8',
    'python-dateutil',
    'pytz',
    'python3-memcached',
    'pyyaml',
    'coverage==3.6',
    'tornado==3.2'
]

#
# Setuptools configuration, used to create python .eggs and such.
# See: http://bashelton.com/2009/04/setuptools-tutorial/ for a nice
# setuptools tutorial.
#

setup(
    name="vcenter_api",
    version="0.1",

    # packaging infos
    package_data={'': ['*.yaml', '*.html', '*.css', '*.js']},
    packages=find_packages(exclude=['test', 'test.*']),

    # dependency infos
    install_requires=install_requires,

    entry_points={
        'console_scripts': [
            'rest_api = app.lib.main:main'
        ]
    },

    zip_safe=False
)
