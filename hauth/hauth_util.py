#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import six
import argparse
import getpass

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

opts = {
        'require': {
            'username': 'your username',
            'password': 'your password',
            }
        }

def config_profile(editor='vi'):
    import os
    import pit
    # set ENVIRON
    if not os.environ.get('EDITOR'):
        os.environ['EDITOR'] = editor

    pit.Pit.get('hauth.account', opts)
    

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
        raise
    return ret

def hauthorize(usrname, passwd, url='https://apresia.hosei.ac.jp:4443/cgi-bin/adeflogin.cgi'):
    return post(url, usrname, passwd)

def get_user_properties(from_pit=False):
    if from_pit:
        import pit
        account = pit.Pit.get('hauth.account', opts)
        usrname = account['username']
        passwd = account['password']
    else:
        usrname = six.moves.input('User name: ')
        passwd = getpass.getpass()
    # strip back-slash
    usrname = usrname.replace('\\', '')
    passwd = passwd.replace('\\', '')
    return usrname, passwd
