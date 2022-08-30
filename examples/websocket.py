import asyncio

from pyevonic.evonic import Evonic


async def main():
    async with Evonic("192.168.1.190") as ev:
        await ev.connect()
        if ev.connected:
            print("Connected!")

        def new_update(device):
            print("Received update from Evonic")
            print(device.__dict__)

        asyncio.create_task(ev.listen(callback=new_update))
        await asyncio.sleep(3600)


if __name__ == "__main__":
    asyncio.run(main())
