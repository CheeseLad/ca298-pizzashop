from django.urls import path
from . import views
from . import forms
from .forms import *

urlpatterns = [
   path('', views.index, name="index"),
   path('order', views.order_pizza, name='order_pizza'),
   path('payment', views.payment, name='payment'),
   path('register/', views.UserSignupView.as_view(), name='register'),
   path('login/',views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm)),
   path('logout/', views.logout_user, name="logout"),
]