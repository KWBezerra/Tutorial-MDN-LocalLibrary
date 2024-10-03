#Add URL maps to redirect the base URL to our application
from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""Configuração de URL do locallibrary

A lista `urlpatterns` roteia URLs para as views. Para mais informações, consulte:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Exemplos:
Views baseadas em função
    1. Adicione uma importação:  from my_app import views
    2. Adicione uma URL à lista urlpatterns:  path('', views.home, name='home')
Views baseadas em classe
    1. Adicione uma importação:  from other_app.views import Home
    2. Adicione uma URL à lista urlpatterns:  path('', Home.as_view(), name='home')
Incluindo outra URLconf
    1. Importe a função include(): from django.urls import include, path
    2. Adicione uma URL à lista urlpatterns:  path('blog/', include('blog.urls'))
"""