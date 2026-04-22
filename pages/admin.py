from django.contrib import admin
from .models import Meslek, UzmanCevap
from .models import Sehir

admin.site.register(Meslek)
admin.site.register(UzmanCevap)


@admin.register(Sehir)
class SehirAdmin(admin.ModelAdmin):
    list_display = ('isim', 'ogrenci_yasam_puani', 'universite_sayisi')
    prepopulated_fields = {'slug': ('isim',)} 