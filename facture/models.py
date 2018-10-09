# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    address = models.TextField()
    zipcode = models.IntegerField()
    city = models.CharField(max_length=80)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Produit(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    reference = models.CharField(max_length=14)
    price = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.name, self.price)

    class Meta:
        ordering = ('name', 'description', 'price')

class Devis(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    facture = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural="Devis"

    def __str__(self):
        return "%s" % (self.client)

class Ligne(models.Model):
    quantity = models.IntegerField()
    produit = models.ForeignKey(Produit, null=True, blank=True)
    facture = models.ForeignKey(Devis, null=True, blank=True)
