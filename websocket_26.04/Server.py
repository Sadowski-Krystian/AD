import asyncio
import websockets
from NetUtl import NetUtl

net = NetUtl()
ip = net.getIp()
port = 8765

async def echo(es, arg=None):
    print(ws)
    async for msg in ws:
        print(msg)
        print(ws.remote_address)

async def main():
    print("Serwer started @ "+ip+": "+str(port))
    async with websockets.serve(echo, ip, port):
        await asyncio.Future()

# print(port)s
# py 3.6
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# py 3.7
asyncio.run(main())