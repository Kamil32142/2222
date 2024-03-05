from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_detail),
    path('', views.item_list)
]