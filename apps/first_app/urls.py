from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
  url(r'^$', views.main),     # This line has changed!
  url(r'^register$', views.register),
  url(r'^login$', views.login),
  url(r'^travels$', views.travels),
  url(r'^travels/destination/(?P<id>\d+)$', views.destination),
  url(r'^travels/add$', views.add_travel_plan),
  url(r'^process_add$', views.process_add),
  url(r'^join/(?P<id>\d+)$', views.join),
  url(r'^logout$', views.logout)
]