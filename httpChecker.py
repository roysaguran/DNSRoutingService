#!/usr/bin/env python
# coding=utf-8

__author__    = "Roy Saguran, roy.saguran@pinoylinux.org"
__copyright__ = "(c) 2016 Alias John Lawrence"
__license__   = "New BSD License"

import _socket
import httplib
import sys

def httpCheck(site, page):
        try:
                conn = httplib.HTTPConnection(site[0],80)
                conn.request("HEAD",page)
                res = conn.getresponse()
                print site[0], res.status, res.reason
        except StandardError:
                return 0

# Open the file with read only permit
try:
        file2Open = open('servers.list', "r")

except IOError:
        print("Cannot open specified file\n")

try:
        for lines in file2Open.readlines():
                stripComment=lines.strip()
                if not stripComment.startswith("#"):
                        site=[lines.rstrip()]
                        page="/"
                        # Call httpCheck Function the checks website status
                        httpCheck(site, page);
except KeyboardInterrupt:
        print('Terminated\n')
