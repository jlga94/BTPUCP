from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.reports, name='index'),
  url(r'^reportes/$', views.reports, name='reports'),
  url(r'^logout/$', views.logout_view, name='logout'),
]