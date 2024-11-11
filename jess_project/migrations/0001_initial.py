# Generated by Django 4.2 on 2024-11-10 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pesanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('waktu', models.DateTimeField()),
                ('catatan', models.TextField()),
                ('status_pesanan', models.CharField(choices=[('pesanan_masuk', 'Pesanan Masuk'), ('diproses', 'Diproses'), ('selesai', 'Selesai')], default='pesanan_masuk', max_length=20)),
                ('nama_pesanan', models.CharField(max_length=255)),
                ('qty', models.IntegerField()),
            ],
        ),
    ]