from django.urls import path
from . import views

app_name = 'almox'

urlpatterns = [
    path('', views.complist, name='list'),
    path('comp/<int:id>', views.compview, name="comp-view"),
    path('addcomp/', views.addcomp, name='add-comp'),
    path('edit/<int:id>', views.editcomp, name='edit-comp'),
    path('comp/delete/<int:id>', views.deletecomp, name='delete-comp'),
    path('addmod/', views.addmod, name='add-mod'),
    path('addloc/', views.addloc, name='add-loc'),
]