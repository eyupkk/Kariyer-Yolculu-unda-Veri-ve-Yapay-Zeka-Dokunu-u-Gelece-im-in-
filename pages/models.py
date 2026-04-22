from django.db import models

class Meslek(models.Model): 
    isim = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    kategori = models.CharField(max_length=50)
    aciklama = models.TextField()

    def __str__(self):
        return self.isim

class UzmanCevap(models.Model):
    meslek = models.ForeignKey(Meslek, on_delete=models.CASCADE, related_name='cevaplar')
    uzman_adi = models.CharField(max_length=100)
    soru = models.TextField()
    cevap = models.TextField()
    memnuniyet_skoru = models.IntegerField(default=10)
    ortalama_maas = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.meslek.isim} - {self.uzman_adi}"



class Sehir(models.Model):
    isim = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, help_text="URL'de görünecek isim (Örn: istanbul)")
    resim = models.ImageField(upload_to='sehirler/', blank=True, null=True)
    tanitim = models.TextField(help_text="Şehir hakkında kısa bir ön bilgi")
    ogrenci_yasam_puani = models.IntegerField(default=5, help_text="1-10 arası bir puan verin")
    ortalama_kira = models.CharField(max_length=50, help_text="Örn: 15.000 TL - 20.000 TL")
    universite_sayisi = models.IntegerField(default=1)

    def __str__(self):
        return self.isim
    
    