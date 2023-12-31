from django.urls import path
from djangoTestDemo.objects_posts import views

urlpatterns = (
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('edit/<int:pk>', views.edit, name="edit"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('found/<int:pk>', views.found, name="found")
)
