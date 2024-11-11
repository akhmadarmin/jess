from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Pesanan
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    return HttpResponse('Selamat Datang')

def kasir(request):
    pesanan_list = Pesanan.objects.all()
    order_terbaru = Pesanan.objects.last()
    context = {
        'title': 'Apps Kasir',
        'pesanan_list': pesanan_list,
        'order_id': order_terbaru.order_id if order_terbaru else "Belum ada order terbaru"
    }
    return render(request, 'kasir.html', context)

def kitchen(request):
    pesanan_list = Pesanan.objects.all()
    context = {
        'title': 'Apps Kitchen',
        'pesanan_list': pesanan_list  
    }
    return render(request, 'kitchen.html', context)

@csrf_exempt
def add_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nama_pesanan = data.get('nama_pesanan')
        qty = data.get('qty')
        
        new_order = Pesanan.objects.create(
            waktu=data.get('waktu'),
            catatan=data.get('catatan', ''),
            status_pesanan='pesanan_masuk',
            nama_pesanan=nama_pesanan,
            qty=qty
        )

        return JsonResponse({
            'order_id': new_order.order_id,
            'nama_pesanan': new_order.nama_pesanan,
            'qty': new_order.qty,
            'status_pesanan': new_order.get_status_pesanan_display()
        })
    return JsonResponse({'error': 'Invalid request'}, status=400)