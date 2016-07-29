# hauth
Authorization Helper for H. Univ.

## Install
You can install via pip command.
```
pip install git+https://github.com/DaikiShimada/hauth.git
```

## How to use
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

## With pit
To avoid typing your username and password everytime, you can use pit module. 

### Install pit for Python3 and Configure your account
```sh
./pit_install.sh
python -c import hauth; hauth.config_profile(editor='vi')
```

### Get user properties from pit
Just choice `from_pit` option!!
```python
import hauth
name, passwd = hauth.get_user_properties(from_pit=True)
hauth.hathorize(name, passwd)
```

More detail is in [example](example) code.

## License
The MIT License (MIT)
