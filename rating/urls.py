from django.urls import re_path
from .views import rating_api

urlpatterns = [
    re_path(r'^rating/$', rating_api),            # For GET all and POST
    re_path(r'^rating/(?P<id>\d+)/$', rating_api), # For PUT and DELETE by ID
]
