# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Client, Produit, Ligne, Devis

# Register your models here.
class LigneAdmin(admin.StackedInline):
    model = Ligne

class DevisAdmin(admin.ModelAdmin):
    list_display=('client',)
    inlines=[LigneAdmin,]

admin.site.register(Devis, DevisAdmin)

admin.site.register(Produit)


admin.site.register(Ligne)



class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address', 'city', 'zipcode')

admin.site.register(Client, ClientAdmin)
