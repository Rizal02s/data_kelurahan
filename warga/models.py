from django.db import models

# Create your models here.
class Warga(models.Model):
    nik=models.CharField(max_length=16, unique=True,verbose_name="Nomor Induk Kependudukan")
    nama=models.CharField(max_length=100, unique=True,verbose_name="Nama lengkap")
    alamat=models.TextField(verbose_name="Alamat Rumah")
    no_telepon=models.CharField(max_length=16, blank=True,verbose_name="Nomor Telepon")
    tanggal_registrasi=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nama

class Pengaduan(models.Model):
    STATUS_CHOICES = [
        ('BARU', 'Baru'),
        ('PROSES', 'Dalam Proses'),
        ('SELESAI', 'Selesai'),
    ]
    aduan = models.CharField(max_length=200, verbose_name="Judul Pengaduan")
    isi = models.TextField(verbose_name="Isi Pengaduan")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='BARU', verbose_name="Status Pengaduan")
    tanggal_aduan = models.DateTimeField(auto_now_add=True)
    
    pelapor = models.ForeignKey(Warga, on_delete=models.CASCADE, related_name='pengaduan', verbose_name="Pelapor")
    
    def __str__(self):
        return self.aduan