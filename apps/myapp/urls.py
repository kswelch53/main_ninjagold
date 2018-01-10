#app-level url code:
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index), #goes to root route
    url(r'^clear$', views.clear),
    url(r'^processmoney$', views.processmoney), #goes to process money view method

]
