from django.urls import path
from . import views

app_name = 'almox'

urlpatterns = [
    path('', views.complist, name='list'),
    path('comp/<int:id>', views.compview, name="comp-view"),
    path('addcomp/', views.addcomp, name='add-comp'),
]