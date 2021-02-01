#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:27:18 2021

@author: samuelgloss and nickpandelakis
"""

import sys
import argparse
import flask
import json

app = flask.Flask(__name__)

@app.route('/games')

def each_olympics_list():
    pass



@app.route('/nocs')

def each_NOC_list():
    pass


@app.route('/medalists/games/<games_id>?[noc=noc_abbreviation]')

def medalist_list():
    pass

