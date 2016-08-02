#!/usr/bin/python
import hauth
name, passwd = hauth.get_user_properties(from_pit=True)
hauth.hathorize(name, passwd)
