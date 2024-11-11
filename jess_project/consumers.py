import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Pesanan

class KitchenConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("order_updates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("order_updates", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        
        # cek jika 'order_id' dan 'status_pesanan' ada dalam data
        if 'order_id' in data and 'status_pesanan' in data:
            order_id = data['order_id']
            status_pesanan = data['status_pesanan']
            
            # perbarui status_pesanan di database models PEsanan
            try:
                pesanan = await Pesanan.objects.aget(order_id=order_id)
                pesanan.status_pesanan = status_pesanan
                await pesanan.asave()
                
                # buat kirim update status ke grup
                await self.channel_layer.group_send(
                    "order_updates",
                    {
                        'type': 'order_status_update',
                        'order_id': order_id,
                        'status_pesanan': status_pesanan,
                    }
                )
            except Pesanan.DoesNotExist:
                print(f"Pesanan dengan order_id {order_id} tidak ditemukan.")

    async def order_status_update(self, event):
        # send data ke WebSocket
        await self.send(text_data=json.dumps({
            'order_id': event['order_id'],
            'status_pesanan': event['status_pesanan']
        }))
