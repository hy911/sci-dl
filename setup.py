#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os

from setuptools import setup, find_packages

# Package meta-data.
NAME = 'sci-dl'
DESCRIPTION = 'sci-dl: help you download SciHub PDF programmatically'
URL = 'https://github.com/soultoolman/sci-dl'
EMAIL = 'soultooman@gmail.com'
AUTHOR = 'soultoolman'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.1.3'

# What packages are required for this module to be executed?
REQUIRED = [
    'requests',
    'beautifulsoup4',
]

# What packages are optional?
EXTRAS = {
    'cmd': [
        'appdirs',
        'click',
        'validators',
        'rich',
        'pysocks',
    ]
}


# What packages are required for testing
TESTS_REQUIRE = [
    'pytest'
]


# console scripts
CONSOLE_SCRIPTS = [
    'sci-dl=sci_dl.main:sci_dl'
]

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier
# for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    # If your package is a single module, use this instead of 'packages':
    packages=find_packages(exclude=['tests']),

    entry_points={
        'console_scripts': CONSOLE_SCRIPTS
    },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    tests_require=TESTS_REQUIRE,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
    # $ setup.py publish support.
    cmdclass={
    },
)
