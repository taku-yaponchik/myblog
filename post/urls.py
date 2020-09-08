from django.urls import path
from .views import *

urlpatterns = [
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/<str:slug>', TagDetail.as_view(), name='tag_detail_url'),
    path('', post_list, name='post_list'),
    path('<slug:post>/', post_detail, name='post_detail'),

]

