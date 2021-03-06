from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('trains/<int:train_id>/location/', views.insert_train, name='insert_train'),
    path('trains/', views.display_trains, name='display_trains'),
    # path('display_trains/', views.display_trains, name='display_trains'),
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='train_data/login.html')),
    path('logout/', auth_views.LogoutView.as_view(next_page='..')),
    path('register/', views.register, name='register')
]
