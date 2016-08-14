#!/usr/bin/env python
from autobahn.asyncio.websocket import \
    WebSocketServerProtocol, WebSocketServerFactory

import asyncio
import asyncio_redis
import redis
import os

_redis_ = os.getenv('REDIS_SVR') or 'localhost'

class BroadcastServerProtocol(WebSocketServerProtocol):
    def __init__(self, *args, **kwargs):
        self.loop = asyncio.get_event_loop()

    def onOpen(self):
        self.factory.register(self)
        self.loop.create_task(self.relay_message())

    def onMessage(self, payload, isBinary):
        if not isBinary:
            self.factory.broadcast(payload.decode('utf8'), self)

    def connectionLost(self, reason):
        WebSocketServerProtocol.connectionLost(self, reason)
        self.factory.unregister(self)

    async def relay_message(self):
        self.red = await asyncio_redis.Connection.create(host=_redis_)
        self.sub = await self.red.start_subscribe()
        await self.sub.subscribe(['chat'])
        while True:
            msg = await self.sub.next_published()
            self.sendMessage(msg.value.encode('utf-8'))


class BroadcastServerFactory(WebSocketServerFactory):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.red = redis.StrictRedis(host=_redis_)
        self.clients = []

    def register(self, client):
        if client not in self.clients:
            print("registered client {0}".format(client.peer))
            self.clients.append(client)

    def unregister(self, client):
        if client in self.clients:
            print("unregistered client {0}".format(client.peer))
            self.clients.remove(client)

    def broadcast(self, msg, client):
        print("broadcasting message '{0}' ..".format(msg))
        self.red.publish('chat', msg.encode('utf-8'))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    factory = BroadcastServerFactory(url=u"ws://0.0.0.0:8000", loop=loop)
    factory.protocol = BroadcastServerProtocol

    coro = loop.create_server(factory, '0.0.0.0', 8000)
    server = loop.run_until_complete(coro)
    print("Server running on 8000...")

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
