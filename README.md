[![PyPI](https://img.shields.io/badge/PyPi-v1.0.0-f39f37.svg)](https://pypi.python.org/pypi/bshare)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/nikhilkumarsingh/bshare/blob/master/LICENSE.txt)

# bshare

A command line bluetooth file sharing application for Linux.

## Installation

- Linux packages required:

	- [bluetooth](http://www.bluez.org/)
	- [libbluetooth-dev](https://packages.ubuntu.com/xenial/libbluetooth-dev)
	- [bluez-tools](https://packages.ubuntu.com/xenial/utils/bluez-tools)
  
	Install as:
	```
	$ sudo apt-get install bluetooth libbluetooth-dev bluez-tools
	```

- To install bshare, simply,

	```
	$ pip install bshare
	```

## Usage

- Help command:

	```
	$ bshare -h

	usage: bshare.py [-h] [-a address] [-s address] [-d] [-l]

	A simple bluetooth file sharer!

	optional arguments:
	  -h, --help            show this help message and exit
	  -a address, --addr address
	                        Connect to bluetooth device with specified Bluetooth
	                        address.
	  -s address, --set address
	                        Set default Bluetooth address.
	  -d, --default         Shows the default bluetooth address.
	  -l, --list            Shows all the added bluetooth devices identified by your
	                        device.

	```

- To list all the added buetooth devices:

	```
	$ bshare -l

	Added devices:
	Windows Phone (9C:6C:15:01:EA:41)
	Videocon V1550 (00:67:1B:BA:7F:B2)
	```

- To share files with a device by specifying its bluetooth address:
	
	```
	$ bshare -a F4:F5:24:B2:D9:7D
	```

- To set a bluetooth address as default (for quick sharing):

	```
	$ bshare -s F4:F5:24:B2:D9:7D

	Default bluetooth address was changed to F4:F5:24:B2:D9:7D
	```

	Now, to share files with device having default bluetooth address, simply:

	```
	$ bshare
	```

- To show default bluetooth address:
	
	```
	$ bshare -d

	Default bluetooth address: F4:F5:24:B2:D9:7D
	```
