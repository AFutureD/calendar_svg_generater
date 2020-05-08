#!/usr/bin/env python
# coding=utf-8
import logging

from flask import Flask
from flask import request
from flask import make_response
from datetime import datetime
import flask

try:
    from urllib.parse import urlparse, urlencode
except ImportError:
    from urlparse import urlparse

app = Flask(__name__)

base_path = ''

@app.route('/', methods=['GET', 'POST'])
def home():
    resp = make_response('<h1>Home Flask<h1>', 200)
    return resp

@app.route('/calendar.svg', methods=('GET', 'HEAD'))
def circle_thin_custom_color():
    """Thin circle with the color set by a global variable."""

    if 'date' in request.args.keys():
        show_date = datetime.strptime(request.args.get('date'),"%Y-%m-%d")
    else:
        show_date = datetime.now()

    return flask.Response(
        """
<svg xmlns="http://www.w3.org/2000/svg" aria-label="Calendar" role="img" viewBox="0 0 512 512">
    <path d="M512 455c0 32-25 57-57 57H57c-32 0-57-25-57-57V128c0-31 25-57 57-57h398c32 0 57 26 57 57z" fill="#e0e7ec" />
    <path d="M484 0h-47c2 4 4 9 4 14a28 28 0 1 1-53-14H124c3 4 4 9 4 14A28 28 0 1 1 75 0H28C13 0 0 13 0 28v157h512V28c0-15-13-28-28-28z" fill="#dd2f45" />
    <g fill="#f3aab9">
        <circle cx="470" cy="142" r="14" />
        <circle cx="470" cy="100" r="14" />
        <circle cx="427" cy="142" r="14" />
        <circle cx="427" cy="100" r="14" />
        <circle cx="384" cy="142" r="14" />
        <circle cx="384" cy="100" r="14" /></g>
    <text id="month" x="32" y="164" fill="#fff" font-family="monospace" font-size="140px" style="text-anchor: left">{month}</text>
    <text id="day" x="256" y="400" fill="{color}" font-family="monospace" font-size="256px" style="text-anchor: middle">{day}</text>
    <text id="weekday" x="256" y="480" fill="#66757f" font-family="monospace" font-size="64px" style="text-anchor: middle">{week}</text>
</svg>
        \n""".format(
            color="black",
            month = show_date.strftime("%b").upper(),
            day = show_date.strftime("%-d"),
            week = show_date.strftime("%A")
        ),
        mimetype='image/svg+xml'
    )

def handler(environ, start_response):
	# 如果没有使用自定义域名
    if environ['fc.request_uri'].startswith("/2016-08-15/proxy"):
        parsed_tuple = urlparse(environ['fc.request_uri'])
        li = parsed_tuple.path.split('/')
        global base_path
        if not base_path:
            base_path = "/".join(li[0:5])

        context = environ['fc.context']
        environ['HTTP_HOST'] = '{}.{}.fc.aliyuncs.com'.format(context.account_id, context.region)
        environ['SCRIPT_NAME'] = base_path + '/'

    return app(environ, start_response)

