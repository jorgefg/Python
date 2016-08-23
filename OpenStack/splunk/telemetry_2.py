#!/usr/bin/env python

import requests
import json
import auth
import datetime

URL, HEADERS = auth.plugin("ceilometer")

t = str(datetime.datetime.now())
delta = datetime.delta(hours=1)

print(t)

data = "{\"filter\": \"{\\\">\\\":{\\\"timestamp\\\":\\\""+t+"\\\"}}\", \"orderby\" : \"[{\\\"timestamp\\\": \\\"DESC\\\"}]\"}"

print(data)
