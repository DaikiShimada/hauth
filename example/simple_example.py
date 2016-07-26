# -*- coding: utf-8 -*-

from __future__ import print_function
import hauth
import logging

if __name__ == '__main__':
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    formatter = logging.Formatter(fmt='%(asctime)s  %(levelname)s %(message)s',
                                  datefmt='%Y/%m/%d %p %I:%M:%S',)
    handler.setFormatter(formatter)

    check_auth = False
    while not check_auth:
        # get username and password
        name, passwd = hauth.get_user_properties()
        check_auth = hauth.hauthorize(name, passwd)
        if check_auth:
            logger.debug('Authorization Success!!')
        else:
            logger.debug('Authorization Failure, Try again.')
