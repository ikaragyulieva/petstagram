from django.urls import path, include
from petstagram.pets import views

urlpatterns = (
    path('add/', views.add_pet),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.pet_details),
        path('edit/', views.edit_pet),
        path('delete/', views.delete_pet),
    ])),
)
