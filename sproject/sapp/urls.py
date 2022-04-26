
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name="home"),
    path('login/',views.loginn, name="login"),
    path('  signup/',views.signup,name="signup"),
    path('profile/',views.profile,name= 'profile'),
    path('logout/',views.logoutt,name= 'logout'),
]