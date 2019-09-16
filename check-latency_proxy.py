#!/bin/python
# -*- coding: utf-8 -*-

import requests
import time
import sys


init_time=round(time.time(), 1)

# do surfing
proxies = {'http': 'http://187.141.164.242:31120'} # Please Change The Proxy Host/Port
print("Using HTTP proxy {0}".format(proxies['http'])) # display proxy address
print(requests.get('http://ifconfig.me/ip', proxies=proxies).text)

end_time=round(round(time.time(), 1) - init_time, 1)

print("latency: {0} s".format(end_time))
