from django.urls import path
from .views import *


urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("services/", services, name="services"),
    path("works/", works, name="works"),
    path("contact/", contact, name="contact"),
    path("download-cv/", download_cv, name="download_cv"),
]
