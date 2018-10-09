# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSet
from extra_views.generic import GenericInlineFormSet
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView, TemplateView
from django.db.models import Q
from .models import Client, Produit, Devis, Ligne

class IndexView(TemplateView):
    template_name = "facture/index.html"


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("index")

class ClientDetailView(DetailView):
    model = Client


class ClientListView(ListView):
    model = Client
    template_name = 'facture/listing_client.html'

    def get_queryset(self):
       query =self.request.GET.get('q', None)
       if query != None:
           return Client.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
       else:
           return Client.objects.all()

class ClientUpdateView(UpdateView):
    model = Client
    fields = ('first_name', 'last_name', 'address', 'zipcode', 'city')
    template_name = 'facture/client_update.html'

    def get_success_url(self):
        return reverse('client', args=[self.object.slug])

class ClientCreateView(CreateView):
    model = Client
    fields =  ('first_name', 'last_name', 'address', 'zipcode', 'city', 'slug')
    template_name = 'facture/client_create.html'

    def get_success_url(self):
        return reverse('client', args=[self.object.slug])

class ProduitCreateView(CreateView):
    model = Produit
    fields =  "__all__"
    template_name = 'facture/produit_create.html'
    success_url = reverse_lazy("produitlist")


class ProduitDetailView(DetailView):
    model = Produit

class ProduitUpdateView(UpdateView):
    model = Produit
    fields = "__all__"
    template_name = 'facture/produit_update.html'

    def get_success_url(self):
        return reverse('produit', args=[self.object.id])

class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = 'facture/produit_confirm_delete.html'
    success_url = reverse_lazy("produitlist")

class ProduitListView(ListView):
    model = Produit
    template_name = 'facture/listing_produit.html'

    def get_queryset(self):
       query =self.request.GET.get('q', None)
       if query != None:
           return Produit.objects.filter(Q(name__icontains=query) | Q(reference__icontains=query))
       else:
           return Produit.objects.all()


class ProduitInline(InlineFormSet):
    model = Produit


class LigneInline(InlineFormSet):
    model = Ligne
    fields = "__all__"


class DevisCreateView(CreateWithInlinesView):
    model = Devis
    inlines = [LigneInline, ]
    fields = "__all__"

    def get_success_url(self):
        return "/"
