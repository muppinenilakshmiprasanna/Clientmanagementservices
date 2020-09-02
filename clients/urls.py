
from django.urls import path

from .views import (
    ClientListView,
    ClientUpdateView,
    ClientDetailView,
    ClientDeleteView,
    ClientCreateView,  # new
    VehicleCreateView, VehicleUpdateView, VehicleDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView)

urlpatterns = [
    path('<int:pk>/edit/',
         ClientUpdateView.as_view(), name='client_edit'),
    path('<int:pk>/',
         ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/delete/',
         ClientDeleteView.as_view(), name='client_delete'),
    path('new/', ClientCreateView.as_view(), name='client_new'),
    path('', ClientListView.as_view(), name='client_list'),

#VEHICLES URLS
   # path('<int:pk>/vehicle/add', VehicleCreateView.as_view(), name='vehicle_new'),
    #path('<int:clientPk>/vehicle/edit/<int:pk>', VehicleUpdateView.as_view(), name='vehicle_edit'),
    #path('<int:clientPk>/vehicle/delete/<int:pk>', VehicleDeleteView.as_view(), name='vehicle_delete'),

    #comments urls
    #path('<int:clientPk>/comment/add', CommentCreateView.as_view(), name='comment_new'),
    #path('<int:clientPk>/comment/edit/<int:pk>', CommentUpdateView.as_view(), name='comment_edit'),
    #path('<int:clientPk>/comment/delete/<int:pk>', CommentDeleteView.as_view(), name='comment_delete'),


    ]


