# -*- coding: utf-8 -*-

import six
import argparse
import getpass

from logging import getLogger,StreamHandler,WARNING
logger = getLogger(__name__)
#handler = StreamHandler()
#handler.setLevel()
logger.setLevel(WARNING)
#logger.addHandler(handler)

def post(url, usrname, passwd):
    ret = False
    try:
        params = six.moves.urllib.parse.urlencode({"name":usrname, "pass":passwd})
        params = params.encode('utf-8')

        headers ={
            "pragma":"no-cache",
            "User-Agent":"Opera/9.80 (Windows NT 6.1; U; ja) Presto/2.10.229 Version/11.60",
        }
        req = six.moves.urllib.request.Request(url, params ,headers)
        res = six.moves.urllib.request.urlopen(req)

        resBody = str(res.read())
        ret = "(s)" in resBody

    except six.moves.urllib.error.URLError as e:
        logger.error(e)
        ret = False
    return ret


def hauthorize(usrname, passwd):
    url = "https://apresia.hosei.ac.jp:4444/cgi-bin/adeflogin.cgi"
    post(url, usrname, passwd)


def get_user_properties():
    usrname = six.moves.input('User name: ')
    passwd = getpass.getpass()
    return usrname, passwd
