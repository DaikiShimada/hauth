# hauth
Authorization Helper for H. Univ.

## Install
You can install via pip command.
> pip install git+https://github.com/DaikiShimada/hauth.git

# How to use
This module has just two methods for you.  
If you want to login H. Univ. network system, call following the methods:
> import hauth
> # call username and password interface
> name, passwd = hauth.get_user_propaties()
> # authorize!!
> hauth.hathorize(name, passwd)

More detail is in example code.

# Lisence
The MIT License (MIT)
