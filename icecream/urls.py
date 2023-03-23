from django.contrib import admin
from django.urls import path
from icecream import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path("home",views.home,name="home"),
    # path("",views.index, name="index"),
    path("",views.login,name="login"),
    
    path("home",views.home, name="home"),
    
    path("contact",views.contact,name="contact"),
    path("services",views.services,name="services"),
    path("login",views.login,name="login"),
    path("signup",views.signup,name="signup"),
    path("logout",views.logout,name="logout"),
    path("contact_2",views.contact_2,name="contact_2")
    




]