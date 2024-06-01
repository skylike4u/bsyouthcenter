from django.urls import path
from blogs.views import PostListView

app_name = "core"

urlpatterns = [path("", PostListView.as_view(), name="home")]
