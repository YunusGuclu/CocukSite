from django.db import models

class Aktivite(models.Model):
    baslik = models.CharField(max_length=200)
    aciklama = models.TextField()
    kategori = models.CharField(max_length=100)
    resim_url = models.URLField(blank=True)
    yas_grubu = models.CharField(max_length=50)
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.baslik

class DenemeyeGeldi(models.Model):
    baslik = models.CharField(max_length=200)
    malzemeler = models.TextField()
    adimlar = models.TextField()
    sure = models.CharField(max_length=50)
    zorluk = models.CharField(max_length=50)
    guvenlik_notu = models.TextField()
    video_url = models.URLField(blank=True)
    sonuc_aciklamasi = models.TextField()

    def __str__(self):
        return self.baslik

class HikayeMasallar(models.Model):
    baslik = models.CharField(max_length=200)
    tur = models.CharField(max_length=100)  # hikaye, masal, fabl
    icerik = models.TextField()
    yazar = models.CharField(max_length=200)
    okuma_suresi = models.CharField(max_length=50)
    yas_grubu = models.CharField(max_length=50)
    sesli_hikaye_url = models.URLField(blank=True)
    anahtar_kelimeler = models.CharField(max_length=500)

    def __str__(self):
        return self.baslik

class BilmeceBulmaca(models.Model):
    tur = models.CharField(max_length=100)  # bilmece, bulmaca, tekerleme
    soru = models.TextField()
    cevap = models.CharField(max_length=500)
    zorluk = models.CharField(max_length=50)
    ipucu = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.soru

class DogaBilgisi(models.Model):
    baslik = models.CharField(max_length=200)
    kategori = models.CharField(max_length=100)  # Hayvanlar, Bitkiler, Çevre
    icerik = models.TextField()
    ilginc_bilgi = models.TextField()
    resim_url = models.URLField(blank=True)
    video_url = models.URLField(blank=True)
    kaynak = models.CharField(max_length=200)

    def __str__(self):
        return self.baslik

class YemekTarifi(models.Model):
    isim = models.CharField(max_length=200)
    zorluk = models.CharField(max_length=50)
    hazirlama_suresi = models.CharField(max_length=50)
    pisirme_suresi = models.CharField(max_length=50)
    malzemeler = models.TextField()
    yapilis = models.TextField()
    besin_degeri = models.TextField()
    resim_url = models.URLField(blank=True)
    video_url = models.URLField(blank=True)
    cocuk_dostu = models.BooleanField(default=True)

    def __str__(self):
        return self.isim


class ElSanatlari(models.Model):
    proje_adi = models.CharField(max_length=200)
    zorluk = models.CharField(max_length=50)
    sure = models.CharField(max_length=50)
    malzemeler = models.TextField()
    yapilis_adimlari = models.TextField()
    yas_grubu = models.CharField(max_length=50)
    resim_url = models.URLField(blank=True)
    video_url = models.URLField(blank=True)

    def __str__(self):
        return self.proje_adi