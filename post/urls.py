from django.urls import re_path
from .views import post_api

urlpatterns = [
    re_path(r'^posts/$', post_api, name='post_list_create'),
    re_path(r'^posts/(?P<id>\d+)/$', post_api, name='post_detail_update_delete'),
]
