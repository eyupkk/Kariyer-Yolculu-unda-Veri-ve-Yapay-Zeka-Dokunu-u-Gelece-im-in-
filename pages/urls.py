from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('meslekler/', views.meslekler, name='meslekler'),
    path('sehirler/', views.sehirler, name='sehirler'),
    path('ybs-rehberi/', views.ybs_detay, name='ybs_detay'),

   
    path('meslekler/bilgisayar-muhendisligi/', views.pc_muh_detay, name='pc_muh_detay'),
    path('meslekler/veri-analisti/', views.veri_analisti_detay, name='veri_analisti_detay'),
    path('meslekler/yazilim-muhendisligi/', views.yazilim_detay, name='yazilim_detay'),
    path('meslekler/makine-muhendisligi/', views.makine_detay, name='makine_detay'),
    path('meslekler/endustri-muhendisligi/', views.endustri_detay, name='endustri_detay'),
    path('meslekler/elektrik-elektronik-muhendisligi/', views.elektrik_detay, name='elektrik_detay'),

    
    path('meslekler/tip-fakultesi/', views.tip_detay, name='tip_detay'),
    path('meslekler/dis-hekimligi/', views.dis_detay, name='dis_detay'),
    path('meslekler/hemsirelik/', views.hemsirelik_detay, name='hemsirelik_detay'),
    path('meslekler/eczacilik/', views.eczacilik_detay, name='eczacilik_detay'),
    path('meslekler/fizyoterapi/', views.ftr_detay, name='ftr_detay'),
    path('meslekler/beslenme-ve-diyetetik/', views.diyetisyen_detay, name='diyetisyen_detay'),

    
    path('meslekler/okul-oncesi-ogretmenligi/', views.okul_oncesi_detay, name='okul_oncesi_detay'),
    path('meslekler/ingilizce-ogretmenligi/', views.ingilizce_detay, name='ingilizce_detay'),
    path('meslekler/hukuk/', views.hukuk_detay, name='hukuk_detay'),
    path('meslekler/psikoloji/', views.psikoloji_detay, name='psikoloji_detay'),
    path('meslekler/pdr/', views.pdr_detay, name='pdr_detay'),

    
    path('meslekler/mimarlik/', views.mimarlik_detay, name='mimarlik_detay'),
    path('meslekler/ic-mimarlik/', views.ic_mimarlik_detay, name='ic_mimarlik_detay'),
    path('meslekler/grafik-tasarim/', views.grafik_tasarim_detay, name='grafik_tasarim_detay'),
    path('meslekler/isletme-iktisat/', views.isletme_iktisat_detay, name='isletme_iktisat_detay'),
    path('meslekler/lojistik/', views.lojistik_detay, name='lojistik_detay'),
    path('meslekler/uluslararasi-ticaret/', views.uluslararası_ticaret_detay, name='uluslararasi_ticaret_detay'),

    
    path('meslekler/<slug:slug>/', views.meslek_detay, name='meslek_detay'),

    
    
    path('sehirler/<slug:slug>/', views.sehir_detay, name='sehir_detay'),

    path('analiz/', views.ai_analiz_sonuc, name='ai_analiz'),
]