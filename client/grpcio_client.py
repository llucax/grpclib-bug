import asyncio
import sys

import grpc

import helloworld_pb2
import helloworld_pb2_grpc


async def main(host: str) -> None:
    async with grpc.aio.insecure_channel(f"{host}:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = await stub.SayHello(helloworld_pb2.HelloRequest(name="you"))
    print("Greeter client received: " + response.message)


asyncio.run(main("[::1]" if len(sys.argv) < 2 else sys.argv[1]))
