from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('codes/create/', views.codes_create, name='codes_create'),
    path('codes/list/', views.codes_list, name='codes_list'),
    path('codes/<int:pk>/', views.codes_detail, name='codes_detail'),
    path('codes/search/', views.codes_search, name='codes_search'),
]