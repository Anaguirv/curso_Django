from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('primera/',  include('primeraApp.urls')),
    path('segunda/',  include('segundaApp.urls')),
]
