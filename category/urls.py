from django.urls import re_path
from .views import category_api  # ✅ import the actual view

urlpatterns = [
    re_path(r'^category/$', category_api),
    re_path(r'^category/(?P<id>\d+)/$', category_api),
]
