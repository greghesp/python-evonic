import asyncio
from evonic import Evonic

ev = Evonic("192.168.1.190")


async def main():

    await ev.connect(callback=log)


def log(e):
    print(e.__dict__)


if __name__ == "__main__":
    asyncio.run(main())
