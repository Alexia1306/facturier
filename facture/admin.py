# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Client, Produit, Ligne, Devis

# Register your models here.


admin.site.register(Client)


admin.site.register(Produit)


admin.site.register(Ligne)


admin.site.register(Devis)
