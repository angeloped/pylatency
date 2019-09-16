#!/bin/python
# -*- coding: utf-8 -*-

import requests
import time
import sys


init_time=round(time.time(), 1)

# do surfing
print(requests.get('http://ifconfig.me/ip').text)

end_time=round(round(time.time(), 1) - init_time, 1)

print("latency: {0} s".format(end_time))
