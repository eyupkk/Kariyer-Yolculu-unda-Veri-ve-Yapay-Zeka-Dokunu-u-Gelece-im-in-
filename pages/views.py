from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html')

def meslekler(request):
    return render(request, 'pages/meslekler.html')
def meslek_detay(request, slug):

    context = {
        'meslek_adi': slug.replace('-', ' ').title()
    }
    return render(request, 'pages/meslek-detay.html', context)
def ybs_detay(request):
    return render(request, 'pages/ybs-detay.html')

def pc_muh_detay(request):
    return render(request, 'pages/pc-muh.html')

def veri_analisti_detay(request):
    return render(request, 'pages/veri-analisti.html')

def yazilim_detay(request):
    return render(request, 'pages/yazilim-muh.html')

def makine_detay(request):
    return render(request, 'pages/makine-muh.html')

def endustri_detay(request):
    return render(request, 'pages/endustri-muh.html')

def elektrik_detay(request):
    return render(request, 'pages/elektrik-muh.html')

def tip_detay(request): 
    return render(request, 'pages/tip-detay.html')

def dis_detay(request): 
    return render(request, 'pages/dis-detay.html')

def hemsirelik_detay(request): 
    return render(request, 'pages/hemsirelik-detay.html')

def eczacilik_detay(request): 
    return render(request, 'pages/eczacilik-detay.html')

def ftr_detay(request): 
    return render(request, 'pages/ftr-detay.html')

def diyetisyen_detay(request): 
    return render(request, 'pages/diyetisyen-detay.html')

def okul_oncesi_detay(request): 
    return render(request, 'pages/okul-oncesi-detay.html')

def ingilizce_detay(request): 
    return render(request, 'pages/ingilizce-detay.html')

def hukuk_detay(request): 
    return render(request, 'pages/hukuk-detay.html')

def psikoloji_detay(request): 
    return render(request, 'pages/psikoloji-detay.html')

def pdr_detay(request): 
    return render(request, 'pages/pdr-detay.html')

def mimarlik_detay(request): 
    return render(request, 'pages/mimarlik-detay.html')

def ic_mimarlik_detay(request): 
    return render(request, 'pages/ic-mimarlik-detay.html')

def grafik_tasarim_detay(request): 
    return render(request, 'pages/grafik-tasarim-detay.html')

def isletme_iktisat_detay(request): 
    return render(request, 'pages/isletme-iktisat-detay.html')

def lojistik_detay(request): 
    return render(request, 'pages/lojistik-detay.html')

def uluslararası_ticaret_detay(request): 
    return render(request, 'pages/uluslararasi-ticaret-detay.html')

from django.shortcuts import render, get_object_or_404
from .models import Sehir  


def home(request):
    return render(request, 'pages/home.html')


def sehirler(request):
    sehirler_listesi = Sehir.objects.all() 
    return render(request, 'pages/sehirler.html', {'sehirler': sehirler_listesi})


def sehir_detay(request, slug):
    sehir = get_object_or_404(Sehir, slug=slug)
    return render(request, 'pages/sehir-detay.html', {'sehir': sehir})




from django.shortcuts import render

def ai_analiz_sonuc(request):
    if request.method == 'POST':
        a = int(request.POST.get('a_puan', 0)) # Analitik/Araştırmacı
        g = int(request.POST.get('g_puan', 0)) # Girişimci/Lider
        s = int(request.POST.get('s_puan', 0)) # Sanatçı/Yaratıcı

        skorlar = {'Araştırmacı': a, 'Girişimci': g, 'Sanatçı': s}
        kazanan = max(skorlar, key=skorlar.get)
        toplam = a + g + s
        oran = round((skorlar[kazanan] / toplam) * 100) if toplam > 0 else 0

        # 60+ Meslekli Geniş Havuz
        meslek_havuzu = {
            'Araştırmacı': {
                'baslik': 'Bilim ve Teknoloji Odaklı Kaşif',
                'detay': 'Karmaşık sistemleri analiz etme ve mantık yürütme gücün çok yüksek.',
                'meslekler': [
                    'Tıp Doktoru (Cerrah/Araştırmacı)', 'Yazılım Mühendisi', 'YBS Uzmanı', 
                    'Veri Bilimci', 'Siber Güvenlik Uzmanı', 'Moleküler Biyoloji ve Genetik',
                    'Elektrik-Elektronik Mühendisi', 'Yapay Zeka Uzmanı', 'Eczacılık', 
                    'Psikiyatrist', 'Uzay Bilimleri Mühendisi', 'Nükleer Enerji Uzmanı'
                ]
            },
            'Girişimci': {
                'baslik': 'Stratejik Lider ve Karar Verici',
                'detay': 'Yönetim, ikna ve büyük resmi görme becerilerinle fark yaratıyorsun.',
                'meslekler': [
                    'Hukuk (Avukat/Savcı)', 'İşletme Yöneticisi', 'Diplomat', 'Pazarlama Müdürü',
                    'Uluslararası Ticaret Uzmanı', 'Ekonomist', 'Lojistik Müdürü', 'Pilot',
                    'Gayrimenkul Yatırım Danışmanı', 'Siyaset Bilimci', 'Finans Direktörü', 'Startup Kurucusu'
                ]
            },
            'Sanatçı': {
                'baslik': 'Yaratıcı ve Estetik Vizyoner',
                'detay': 'Dünyayı farklı bir perspektifle görüyor, özgün değerler üretiyorsun.',
                'meslekler': [
                    'Mimarlık', 'Gastronomi ve Mutfak Sanatları', 'Dijital Oyun Tasarımcısı', 
                    'UI/UX Tasarımcı', 'Moda Tasarımcısı', 'Endüstriyel Tasarımcı', 'Reklam Yazarı',
                    'İç Mimarlık', 'Film Yönetmeni', 'Restoratör', 'Sahne Sanatları Uzmanı', 'Animatör'
                ]
            }
        }

        sonuc = meslek_havuzu[kazanan]
        # Sonuç sayfasında boğulmaması için en iyi 4 mesleği seçiyoruz
        sonuc['oneri_listesi'] = sonuc['meslekler'][:4] 
        sonuc['oran'] = oran
        
        return render(request, 'pages/ai_sonuc.html', {'sonuc': sonuc})

    return render(request, 'pages/ai_form.html')