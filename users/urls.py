from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = "users"

# routing
urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("create/", views.UserCreateView.as_view(), name="create"),
    path("detail/<int:pk>", views.UserDetailView.as_view(), name="detail"),
    path("update/<int:pk>", views.UserUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", views.UserDeleteView.as_view(), name="delete"),
]
