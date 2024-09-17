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


class PostDetailView(DeleteView):
    model = Post
    context_object_namae = "post"
    template_name = "blogs/detail.html"
