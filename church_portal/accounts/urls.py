from django.conf.urls import url,include
from django.urls.resolvers import URLPattern
from accounts import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('contact/',views.contact,name="contact"),
    url(r"^accounts/login/$",views.login, name="login"),
    url(r"^accounts/register/$",views.register, name="register"),
    url(r"^accounts/logout/$",views.logout, name="logout"),
]
