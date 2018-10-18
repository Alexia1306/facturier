"""facturier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from facture.views import IndexView, ClientDetailView, ClientUpdateView, ClientCreateView, ClientDeleteView, ClientListView
from facture.views import ProduitCreateView, ProduitDetailView, ProduitUpdateView, ProduitDeleteView, ProduitListView
from facture.views import DevisCreateView, DevisListView, DevisDetailView, DevisEditView,  DevisLineEditView, DevisLineDeleteView, DevisLineAddView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView.as_view()),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page='/')),


    url(r'^client/create/$', ClientCreateView.as_view(), name='clientcreate'),
    url(r'^client/list$', ClientListView.as_view(), name='clientlist'),
    url(r'^client/(?P<slug>[-\w]+)/$', ClientDetailView.as_view(), name='client'),
    url(r'^client/(?P<slug>[-\w]+)/update/$', ClientUpdateView.as_view(), name='clientupdate'),
    url(r'^client/(?P<slug>[-\w]+)/delete/$', ClientDeleteView.as_view(), name='clientdelete'),

    url(r'^produit/create/$', ProduitCreateView.as_view(), name='produitcreate'),
    url(r'^produit/list$', ProduitListView.as_view(), name='produitlist'),
    url(r'^produit/(?P<pk>[\d]+)/$', ProduitDetailView.as_view(), name='produit'),
    url(r'^produit/(?P<pk>[\d]+)/update/$', ProduitUpdateView.as_view(), name='produitupdate'),
    url(r'^produit/(?P<pk>[-\w]+)/delete/$', ProduitDeleteView.as_view(), name='produitdelete'),


    url(r'^devis/ligne/delete/$', DevisLineDeleteView.as_view(), name='devis_ligne_delete'),
    url(r'^devis/ligne/add/$', DevisLineAddView.as_view(), name='devis_ligne_add'),
    url(r'^devis/create/$', DevisCreateView.as_view(), name='deviscreate'),
    url(r'^devis/list$', DevisListView.as_view(), name='devislist'),
    url(r'^devis/(?P<pk>[\w]+)/$', DevisDetailView.as_view(), name='devis'),
    url(r'^devis/(?P<field_name>[\w]+)/edit/$', DevisEditView.as_view(), name='devis_edit'),
    url(r'^devis/ligne/(?P<pk>[-\w]+)/(?P<field_name>[-\w]+)/edit/$', DevisLineEditView.as_view(), name='devis_ligne_edit'),
    url(r'^$', IndexView.as_view(), name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
