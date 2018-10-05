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
from facture.views import IndexView, ClientDetailView, ClientUpdateView, ClientCreateView, ClientDeleteView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView.as_view()),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page='/')),
    url(r'^client/(?P<slug>[-\w]+)/$', ClientDetailView.as_view(), name='client'),
    url(r'^update/(?P<slug>[-\w]+)/$', ClientUpdateView.as_view(), name='clientupdate'),
    url(r'^create/$', ClientCreateView.as_view(), name='clientcreate'),
    url(r'^delete/(?P<slug>[-\w]+)/$', ClientDeleteView.as_view(), name='clientdelete'),
    url(r'^$', IndexView.as_view(), name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
