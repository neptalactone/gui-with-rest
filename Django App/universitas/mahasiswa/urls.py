from django.conf.urls import url
from mahasiswa import views

urlpatterns = [
    url(r'^mahasiswa/$', views.list_mahasiswa),
    url(r'^mahasiswa/(?P<nim>[0-9]+)/$', views.detail_mahasiswa),
]
