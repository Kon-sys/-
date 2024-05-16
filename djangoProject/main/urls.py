from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
] + static(settings.STATIC_URL, nt_root=settings.STATIC_ROOT)