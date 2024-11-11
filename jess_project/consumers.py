import json
from channels.generic.websocket import AsyncWebsocketConsumer

class KitchenConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("order_updates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("order_updates", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        order_id = data['order_id']
        status_pesanan = data['status_pesanan']

        await self.channel_layer.group_send(
            "order_updates",
            {
                'type': 'order_status_update',
                'order_id': order_id,
                'status_pesanan': status_pesanan,
            }
        )

    async def order_status_update(self, event):
        await self.send(text_data=json.dumps({
            'order_id': event['order_id'],
            'status_pesanan': event['status_pesanan']
        }))


class KasirConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("order_updates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("order_updates", self.channel_name)

    async def order_status_update(self, event):
        await self.send(text_data=json.dumps({
            'order_id': event['order_id'],
            'status_pesanan': event['status_pesanan']
        }))
