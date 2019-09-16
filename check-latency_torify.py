#!/bin/python
# -*- coding: utf-8 -*-

from torpy.http.requests import TorRequests
import time
import sys


# do surfing
with TorRequests() as tor_requests:
	with tor_requests.get_session() as sess:
		init_time=round(time.time(), 1)
		print(sess.get("http://ifconfig.me/ip", timeout=10).text)


end_time=round(round(time.time(), 1) - init_time, 1)

print("latency: {0} s".format(end_time))
