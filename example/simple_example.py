# -*- coding: utf-8 -*-

from __future__ import print_function
import hauth

# authorize
check_auth = False
while not check_auth:
    # get username and password
    name, passwd = hauth.get_user_propaties()

    check_auth = hauth.authorize(name, passwd):
    if check_auth:
        print('Authorization Success!!')
    else:
        print('Authorization Failure, Try again.')
