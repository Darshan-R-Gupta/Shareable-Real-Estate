from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index,name='home'),
    path('login', views.login,name='Login'),
    path('signup', views.signup,name='Signup'),
    path('Logout', views.logout,name='Logout'),
    path('profile', views.profile, name='profile')
]
