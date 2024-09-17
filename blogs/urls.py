from django.urls import path
from .views import PostListView, PostDetailView, CategoryPostListView

app_name = "blogs"

# routing
urlpatterns = [
    path("list/", PostListView.as_view(), name="list"),
    path("post/<int:pk>", PostDetailView.as_view(), name="detail"),
    # 카테고리별 전체 게시물 페이지
    path(
        "category/<str:category_name>/",
        CategoryPostListView.as_view(),
        name="category_post_list",
    ),
]
