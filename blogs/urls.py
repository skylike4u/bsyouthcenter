from django.views.generic import TemplateView
from django.urls import path


from .views import PostListView, PostDetailView

app_name = "blogs"

# routing
urlpatterns = [
    path("list/", PostListView.as_view(), name="list"),
    path("post/<int:pk>", PostDetailView.as_view(), name="detail"),
]
