import asyncio

import aiohttp
import logging

from pyevonic.evonic import Evonic

logging.basicConfig(level=logging.DEBUG)


async def main():
    session = aiohttp.ClientSession()

    async with Evonic("192.168.1.190", session=session) as ev:
        await ev.connect()
        if ev.connected:
            print("Connected!")

        def new_update(device):
            print("Received update from Evonic")
            print(device.__dict__)

        asyncio.create_task(ev.listen(callback=new_update))
        await ev.set_temperature(19)
        await asyncio.sleep(3600)


if __name__ == "__main__":
    asyncio.run(main())
