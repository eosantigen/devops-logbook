from django import views
from django.urls import path
from django.views.generic import TemplateView

from devops_logbook.views import Index


urlpatterns = [
    path('', Index.as_view(), name='list'),
]