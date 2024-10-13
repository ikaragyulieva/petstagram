from django.urls import path, include
from petstagram.photos import views

urlpatterns = (
    path('add/', views.add_photo),
    path('<int:pk>/', include([
        path('', views.photo_details),
        path('edit/', views.edit_photo),
    ])),
)
