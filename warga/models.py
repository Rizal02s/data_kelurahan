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