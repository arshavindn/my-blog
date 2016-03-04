from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^articles/([0-9]{4})/$', views.year_archive),
]
