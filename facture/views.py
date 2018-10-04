# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from .models import Client, Produit, Devis, Ligne

class IndexView(ListView):
    model = Client


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("index")

class ClientDetailView(DetailView):
    model = Client
    slug_url_kwarg = 'first_name'
    slug_field = 'first_name'

class ClientUpdateView(UpdateView):
    model = Client
    slug_url_kwarg = 'first_name'
    slug_field = 'first_name'
    fields = ('first_name', 'last_name', 'address', 'zipcode', 'city')
    template_name = 'facture/client_update.html'


class ClientCreateView(CreateView):
    model = Client
    fields =  ('first_name', 'last_name', 'address', 'zipcode', 'city')
    template_name = 'facture/client_create.html'

class UserDetailView(DetailView):
    model = User
    slug_url_kwarg = 'username'
    slug_field = 'username'


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
