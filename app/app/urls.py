from django.contrib import admin
from django.urls import path, include
from main import views
from debug_toolbar.toolbar import debug_toolbar_urls
from app.settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include('main.urls', namespace='main')),
    path('catalog/',  include('goods.urls', namespace='catalog'))
]

if DEBUG:
    urlpatterns += debug_toolbar_urls()
