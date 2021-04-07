import asyncio
import aiohttp


class randomorg:
    def __init__(self, apikey):
        self.loop = asyncio.get_event_loop()
        self.apikey = apikey

    async def GenerateIntegers(self, n, minimum, maximum, base=None):
        if base is None:
            js = {
                "jsonrpc": "2.0",
                "method": "generateIntegers",
                "params": {
                    "apiKey": self.apikey,
                    "n": n,
                    "min": minimum,
                    "max": maximum
                },
                "id": 1
            }
        else:
            js = {
                "jsonrpc": "2.0",
                "method": "generateIntegers",
                "params": {
                    "apiKey": self.apikey,
                    "n": n,
                    "min": minimum,
                    "max": maximum,
                    "base": base
                },
                "id": 1
            }
        async with aiohttp.ClientSession() as session:
            async with session.post("https://api.random.org/json-rpc/4/invoke", json=js) as resp:
                resp = await resp.json(content_type='application/json')
                resp = resp['result']['random']['data']
                return resp

    async def GenerateStrings(self, n, length, characters):
        js = {
            "jsonrpc": "2.0",
            "method": "generateStrings",
            "params": {
                "apiKey": self.apikey,
                "n": n,
                "length": length,
                "characters": characters
            },
            "id": 1
        }
        async with aiohttp.ClientSession() as session:
            async with session.post("https://api.random.org/json-rpc/4/invoke", json=js) as resp:
                resp = await resp.json(content_type='application/json')
                resp = resp['result']['random']['data']
                return resp

    async def GenerateIntegerSequences(self, n, length, minimum, maximum):
        js = {
            "jsonrpc": "2.0",
            "method": "generateIntegerSequences",
            "params": {
                "apiKey": self.apikey,
                "n": n,
                "length": length,
                "min": minimum,
                "max": maximum
            },
            "id": 1
        }
        async with aiohttp.ClientSession() as session:
            async with session.post("https://api.random.org/json-rpc/4/invoke", json=js) as resp:
                resp = await resp.json(content_type='application/json')
                resp = resp['result']['random']['data']
                return resp
