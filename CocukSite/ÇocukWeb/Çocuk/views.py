from django.shortcuts import render, get_object_or_404
from .models import *

def home(request):
    context = {
        'aktiviteler': Aktivite.objects.all()[:4],
        'deneyler': DenemeyeGeldi.objects.all()[:3],  # BilimselDeney yerine DenemeyeGeldi
        'bilmeceler': BilmeceBulmaca.objects.all()[:4],
        'doga_bilgileri': DogaBilgisi.objects.all()[:3]
    }
    return render(request, 'home.html', context)

def yemek_tarifleri(request):
    context = {
        'tarifler': YemekTarifi.objects.all()
    }
    return render(request, 'yemek_tarifleri.html', context)

def el_sanatlari(request):
    context = {
        'projeler': ElSanatlari.objects.all()
    }
    return render(request, 'el_sanatlari.html', context)

def bilmeceler(request):
    context = {
        'bilmeceler': BilmeceBulmaca.objects.all()
    }
    return render(request, 'bilmeceler.html', context)

def hikayeler(request):
    context = {
        'hikayeler': HikayeMasallar.objects.all()
    }
    return render(request, 'hikayeler.html', context)

# Detay sayfaları için view'lar
def aktivite_detay(request, id):
    aktivite = get_object_or_404(Aktivite, id=id)
    context = {
        'aktivite': aktivite,
        'related_aktiviteler': Aktivite.objects.exclude(id=id)[:3]  # İlgili diğer aktiviteler
    }
    return render(request, 'aktivite_detay.html', context)

def deney_detay(request, id):
    deney = get_object_or_404(DenemeyeGeldi, id=id)  # DenemeyeGeldi modelini kullanıyoruz
    context = {
        'deney': deney,
        'related_deneyler': DenemeyeGeldi.objects.exclude(id=id)[:3]  # İlgili diğer deneyler
    }
    return render(request, 'deney_detay.html', context)



def el_sanati_detay(request, id):
    proje = get_object_or_404(ElSanatlari, id=id)
    return render(request, 'el_sanati_detay.html', {'proje': proje})

def yemek_detay(request, id):
    tarif = get_object_or_404(YemekTarifi, id=id)
    return render(request, 'yemek_detay.html', {'tarif': tarif})

def doga_detay(request, id):
    bilgi = get_object_or_404(DogaBilgisi, id=id)
    context = {
        'bilgi': bilgi,
        'related_bilgiler': DogaBilgisi.objects.exclude(id=id).filter(kategori=bilgi.kategori)[:3]
    }
    return render(request, 'doga_detay.html', context)