from django.urls import path
from petstagram.common import views

urlpatterns = (
    path('', views.home, name='home-page'),
    path('like/<int:photo_id>/', views.like_functionality, name='like'),
    path('share/<int:photo_id>', views.copy_link_to_clipboard_functionality, name='share'),
)
