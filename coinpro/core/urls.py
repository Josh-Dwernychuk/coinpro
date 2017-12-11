from django.conf.urls import url
from coinpro.core import views


urlpatterns = [
    url(r'^', views.home, name='core'),
]
