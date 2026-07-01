from django.urls import path
import users.views as views
urlpatterns = [
    path("login/", views.login, name="user_login"),
    path("register/", views.register, name="user_register"),
]