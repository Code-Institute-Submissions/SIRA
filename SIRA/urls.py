"""SIRA URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from home_page.views import homepage
from pages.views import terms_view, privacy_view
from search.views import PostSearchView
from about import urls
from get_involved import urls
from adoptables import urls
from forever_home import urls
from accounts import urls 
from contact import urls
from donation import urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage, name='home'),
    url(r'^terms-and-conditions/$', terms_view, name='terms'),
    url(r'^privacy/$', privacy_view, name='privacy'),
    url(r'^search/', PostSearchView.as_view(), name='search'),
    url(r'^about/', include('about.urls')),
    url(r'^get_involved/', include('get_involved.urls')),
    url(r'^adoptables/', include('adoptables.urls')),
    url(r'^forever_home/', include('forever_home.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^donation/', include('donation.urls')),
    
]

