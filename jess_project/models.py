from django.db import models
from datetime import datetime

class Pesanan(models.Model):
    STATUS_CHOICES = [
        ('pesanan_masuk', 'Pesanan Masuk'),
        ('diproses', 'Diproses'),
        ('selesai', 'Selesai')
    ]
    
    order_id = models.CharField(max_length=6, unique=True, editable=False)
    waktu = models.DateTimeField(auto_now_add=True)
    catatan = models.TextField(blank=True, null=True)
    status_pesanan = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pesanan_masuk'
    )
    nama_pesanan = models.CharField(max_length=255)
    qty = models.IntegerField()
    
    def __str__(self):
        return f"{self.order_id} - {self.nama_pesanan}"

    def save(self, *args, **kwargs):
        if not self.order_id: 
            today = datetime.now()
            date_str = today.strftime('%d%m')
            
            orders_today = Pesanan.objects.filter(
                waktu__year=today.year,
                waktu__month=today.month,
                waktu__day=today.day
            ).count() + 1  # hitung order ke-x untuk hari ini

            # format order_id: "0" + tanggal (2 digit) + bulan (2 digit) + urutan pesanan hari ini (2 digit) yang auto input
            self.order_id = f"0{date_str}{orders_today:02d}"  # buat 2 digit per harian
        super().save(*args, **kwargs)
