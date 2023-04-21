"""
URL configuration for ZeonChita project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from zeon.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_index, name='render_index'),
    path('catalog', render_catalog, name='render_catalog'),
    path('contacts', render_contacts, name='render_contacts'),
    path('info', render_info, name='render_info'),
    path('korzina', render_korzina, name='render_korzina'),
    path('politika', render_politika, name='render_politika'),
    path('pravila', render_pravila, name='render_pravila'),
    path('pred_pokupka', render_pred_pokupka, name='render_pred_pokupka'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
