# path to different webpages

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("concept/", views.concept, name="concept"),
    path("specialiste/", views.specialiste, name="specialiste"),
    path("tarif/", views.tarif, name="tarif"),
    path("instagram/", views.instagram, name="instagram"),
    path("contact/", views.contact, name="contact"),
]