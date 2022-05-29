from django.contrib import admin
from django.urls import path

from data_processing import views

urlpatterns = [
    path("",views.index, name='data_processing'),
    path("visual",views.visualize,name='Visualize'),
    path("custom_query",views.custom_query,name='custom_query'),
    path("visual_4w",views.visual_4w,name='visual_4w'),
    path("visual_ev",views.visual_ev,name='visual_ev'),
]

