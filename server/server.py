#!/usr/bin/env python
from autobahn.asyncio.websocket import \
    WebSocketServerProtocol, WebSocketServerFactory

import asyncio
import redis
import os

_redis_ = os.getenv('REDIS_SVR') or 'localhost'

class BroadcastServerProtocol(WebSocketServerProtocol):

    def onOpen(self):
        self.factory.register(self)

    def onMessage(self, payload, isBinary):
        if not isBinary:
            self.factory.broadcast(payload.decode('utf8'), self)

    def connectionLost(self, reason):
        WebSocketServerProtocol.connectionLost(self, reason)
        self.factory.unregister(self)

    def tryRelayMessage(self):
        if not hasattr(self, 'sub'):
            self.red = redis.StrictRedis(host=_redis_)
            self.sub = self.red.pubsub()
            self.sub.subscribe('chat')
        m = self.sub.get_message()
        if m is not None and m['type'] == 'message':
            print("Relaying %s" % m)
            self.sendMessage(m['data'])


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
        for c in self.clients:
            self.loop.call_soon(c.tryRelayMessage)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    factory = BroadcastServerFactory(url=u"ws://0.0.0.0:7000", loop=loop)
    factory.protocol = BroadcastServerProtocol

    coro = loop.create_server(factory, '0.0.0.0', 7000)
    server = loop.run_until_complete(coro)
    print("Server running on 7000...")

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
