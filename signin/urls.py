from django.urls import path

from . import views  

app_name = 'signin'

urlpatterns = [
    path('', views.login_view, name='ajax_login'),
    path('home/', views.home, name='home'),
]