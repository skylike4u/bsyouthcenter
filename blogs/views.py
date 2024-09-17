# from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView,
)
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormMixin

from .models import Post


class PostListView(ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blogs/list.html"
    paginate_by = 25

    # 각 카테고리 4개만 노출
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        # 특정 카테고리를 필터링 (예: '여행'이라는 카테고리 ID가 1이라고 가정)
        # 각 카테고리별 최신 4개의 게시물 가져오기
        context["health_posts_4pcs"] = Post.objects.filter(categories__name="건강")[:4]
        context["travel_posts_4pcs"] = Post.objects.filter(categories__name="여행")[:4]
        context["food_beverage_posts_4pcs"] = Post.objects.filter(
            categories__name="음식"
        )[:4]
        context["fashion_beauty_posts_4pcs"] = Post.objects.filter(
            categories__name="패션/뷰티"
        )[:4]
        context["miscellaneous_posts_4pcs"] = Post.objects.filter(
            categories__name="그외다양한주제"
        )[:4]
        return context


# 카테고리별 전체 게시물을 보여줄 뷰
class CategoryPostListView(ListView):
    model = Post
    template_name = "blogs/category_list.html"
    context_object_name = "posts"
    paginate_by = 10  # 페이지당 10개의 게시물

    def get_queryset(self):
        # URL에서 전달된 카테고리 이름으로 필터링
        # category_name에서 슬래시(/)를 하이픈(-)으로 변경하여 URL을 생성 (슬래시(/)를 URL에서 처리하기 어렵기 때문에, 슬래시를 -와 같은 문자로 대체하는 방법)
        category_name = self.kwargs.get("category_name").replace("-", "/")
        return Post.objects.filter(categories__name=category_name)

    def get_context_data(self, **kwargs):
        context = super(CategoryPostListView, self).get_context_data(**kwargs)
        context["category_name"] = self.kwargs.get("category_name")
        return context


class PostDetailView(DeleteView):
    model = Post
    context_object_namae = "post"
    template_name = "blogs/detail.html"
