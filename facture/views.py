# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.views.generic import DetailView

class UserDetailView(DetailView):
    model = User
    slug_url_kwarg = 'username'
    slug_field = 'username'

class ClientDetailView(DetailView):
    model = Client
    slug_url_kwarg = 'first_name'
    slug_field = 'first_name'

class ProduitDetailView(DetailView):
    model = Produit
    slug_url_kwarg = 'name'
    slug_field = 'name'

class DevisDetailView(DetailView):
    model = Devis
    slug_url_kwarg = 'facture'
    slug_field = 'facture'

class LigneDetailView(DetailView):
    model = Ligne
    slug_url_kwarg = 'produit'
    slug_field = 'produit'
