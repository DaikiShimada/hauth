# hauth
Authorization Helper for H. Univ.

## Install
You can install via pip command.
```
pip install git+https://github.com/DaikiShimada/hauth.git
```

# How to use
This module has just two methods for you.  
If you want to login H. Univ. network system, call following the methods:
```python
import hauth
# call username and password interface
name, passwd = hauth.get_user_properties()
# authorize!!
hauth.hathorize(name, passwd)
```

If you are one-liner...
```python
import hauth
hauth.hauthorize(*hauth.get_user_properties())
```

More detail is in [example](example/simple_example.py) code.

# License
The MIT License (MIT)
