from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
   url(r'^$', views.index, name='index'),
   path('menu/<int:id>/', views.menu, name='menu'),
   path('menu/<int:id>/edit', views.edit, name='edit'),

]
