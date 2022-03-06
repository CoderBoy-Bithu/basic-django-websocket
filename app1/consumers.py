import json
from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio

class MySyncConsumers(SyncConsumer):

    def websocket_connect(self,event):
        print("WebSocket connected...",event)
        self.send({
            'type':'websocket.accept'
        })
    
    def websocket_receive(self,event):
        print("WebSocket Receive...",event)
        for i in range(10):
            self.send({
            'type':'websocket.send',
            'text': json.dumps({"count": i})
            })
            sleep(1)

    
    def websocket_disconnect(self,event):
        print("WebSocket Disconnect...",event)
        raise StopConsumer()

class MyAsyncConsumers(AsyncConsumer):

    async def websocket_connect(self,event):
        print("WebSocket connected",event)
        await self.send({
            'type':'websocket.accept'
        })
    
    async def websocket_receive(self,event):
        print("WebSocket Receive",event)
        for i in range(10):
            await self.send({
            'type':'websocket.send',
            'text': str(i)
            })
            await asyncio.sleep(1)
    
    async def websocket_disconnect(self,event):
        print("WebSocket Disconnect",event)
        raise StopConsumer()