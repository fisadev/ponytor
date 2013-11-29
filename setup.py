#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='ponytor',
    version='0.1.2',
    description=u'A small command line utility and python lib to run automated things when files change',
    long_description=open('README.rst').read(),
    author = u'Juan Pedro Fisanotti',
    author_email = 'fisadev@gmail.com',
    url='http://github.com/fisadev/ponytor',
    py_modules=['ponytor',],
    entry_points = {'console_scripts': ['ponytor = ponytor:main',],},
    install_requires=['pyinotify',],
    license='LICENSE.txt',
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
