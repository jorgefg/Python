#!/usr/bin/env python

import requests
import json
import auth
import datetime

URL, HEADERS = auth.plugin("ceilometer")

timestamp = str(datetime.datetime.now() - datetime.timedelta(hours=1))

data = "{\"filter\": \"{\\\">\\\":{\\\"timestamp\\\":\\\"" + timestamp + \
       "\\\"}}\", \"orderby\": \"[{\\\"timestamp\\\": \\\"DESC\\\"}]\", \"limit\": 100000}"

response = requests.post(URL + '/v2/query/samples', data=data, headers=HEADERS, verify=False)

t = [["id",
      "metadata",
      "meter",
      "project_id",
      "recorded_at",
      "resource_id",
      "source",
      "timestamp",
      "type",
      "unit",
      "user_id",
      "volume"
    ]]

for line in json.loads(response.text):
    t.append([
        line['id'],
        json.dumps(line['metadata']),
        line['meter'],
        line['project_id'],
        line['recorded_at'],
        line['resource_id'],
        line['source'],
        line['timestamp'],
        line['type'],
        line['unit'],
        line['user_id'],
        line['volume']
    ])

for line in t:
    print("{0};{1};{2};{3};{4};{5};{6};{7};{8};{9};{10};{11}".format(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11]))
