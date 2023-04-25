from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('our-works', views.our_works, name='our_works'),
    path('prices', views.prices, name='prices'),
    path('contacts', views.contacts, name='contacts'),
    path('our-works/<int:pk>', views.WorksDetailView.as_view(), name='works-detail')
]