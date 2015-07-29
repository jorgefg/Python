#!/usr/bin/env python

import sys
from vipr import *

client = ViPR(
        username='root',
        password='ChangeMe1!',
        token_endpoint='https://192.168.10.182:4443/login',
        vipr_endpoint='https://192.168.10.182:4443',
        request_timeout=30,
        verify_ssl=False
    )

print (sys.argv[1])