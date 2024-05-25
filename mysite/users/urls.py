
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("logout/", views.LogoutView.as_view(http_method_names = ['get', 'post', 'options']
                                             ), name="logout")
]