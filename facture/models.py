# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    address = models.TextField()

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

class Facture(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s" % (self.id_Client, self.id_Produit, self.price)

class Ligne(models.Model):
    quantity = models.IntegerField()
    produit = models.ForeignKey(Produit, null=True, blank=True)
    facture = models.ForeignKey(Facture, null=True, blank=True)

    def __unicode__(self):
        return self.label
