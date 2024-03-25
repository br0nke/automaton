from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('discussions/', views.discussion_list, name='discussion_list'),
    path('discussions/<int:pk>/', views.discussion_detail, name='discussion_detail'),
    path('discussion/create/', views.discussion_create, name='discussion_create'),
    path('discussions/<int:discussion_id>/add_post/', views.add_post, name='add_post'),
]
