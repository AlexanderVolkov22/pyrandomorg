Simple Asynchronous Python Library For Random.org API
===============

![PyPI](https://img.shields.io/pypi/v/0.0.1)

Hello, thanks for choosing my library to work with the [random.org](http://api.random.org) API

[Aiohttp](https://github.com/aio-libs/aiohttp) was used as a web client

INSTALLATION
------------

`pip3 install Pyrandomorg`

REQUIREMENTS
-----------

```
python<=3.8
aiohttp<=3.7.3
```

EXAMPLES
---------
```
import asyncio

from pyrandomorg.randomorg import randomorg  # import Library

rdorg = randomorg('<Random.org token here>')


async def main():
    print(await rdorg.GenerateIntegers(1, 2, 3))  # This method generates true random integers within a user-defined range.
    print(await rdorg.GenerateStrings(6, 4, "dfsfdsfsdfsdggfdsgdfgdf"))  # This method generates true random strings.
    print(await rdorg.GenerateIntegerSequences(60, 20, 1, 10)) # This method generates uniform or multiform sequences of true random integers within user-defined ranges.


loop = asyncio.get_event_loop()
app = loop.run_until_complete(main())
```

MORE DETAILS
------------
[Random.org API](https://api.random.org/json-rpc/4/basic)
