from django.urls import path
from . import views

app_name = 'almox'

urlpatterns = [
    path('', views.CompListView.as_view(), name='list'),
]