from django.urls import re_path
from django.views.generic import TemplateView

from core import views

urlpatterns = [
    re_path(r'^reserve/', views.SearchRouteView.as_view(), name="search"),
]
