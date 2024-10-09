"""
URL configuration for meme_generator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from api.views import (
    MemeTemplateListView,
    MemeListView,
    MemeCreateView,
    MemeRetrieveView,
    MemeRateView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/templates/', MemeTemplateListView.as_view(), name='meme-template-list'),  # Add this line
    path('api/memes/', MemeListView.as_view(), name='meme-list'),
    path('api/memes/create/', MemeCreateView.as_view(), name='meme-create'),
    path('api/memes/<int:pk>/', MemeRetrieveView.as_view(), name='meme-detail'),
    path('api/memes/rate/', MemeRateView.as_view(), name='meme-rate'),
]