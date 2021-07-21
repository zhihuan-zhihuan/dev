#!/usr/bin/evn python
# -*- coding:utf-8 -*-

import asyncio
import websockets


async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello world!")
        print("< Hello world!")
        while True:
            recv_text = await websocket.recv()
            print("> {}".format(recv_text))


asyncio.get_event_loop().run_until_complete(
    hello('ws://localhost:8765'))
