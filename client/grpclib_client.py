import asyncio
import sys

from grpclib.client import Channel

import better.helloworld


async def main(host: str) -> None:
    async with Channel(host=host, port=50051) as channel:
        service = better.helloworld.GreeterStub(channel)
        response = await service.say_hello(better.helloworld.HelloRequest(name="world"))
    print(response)


asyncio.run(main("::1" if len(sys.argv) < 2 else sys.argv[1]))
