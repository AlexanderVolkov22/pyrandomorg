Simple Asynchronous Python Library For Random.org API
===============

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

from pyrandomorg import Pyrandomorg  # import Library

randomorg = Pyrandomorg('<Random.org token here>')


async def main():
    print(await randomorg.GenerateIntegers(1, 2, 3))
    print(await randomorg.GenerateStrings(6, 4, "dfsfdsfsdfsdggfdsgdfgdf"))
    print(await randomorg.GenerateIntegerSequences(60, 20, 1, 10))


loop = asyncio.get_event_loop()
app = loop.run_until_complete(main())
```

MORE DETAILS
------------
[Random.org API](https://api.random.org/json-rpc/4/basic)