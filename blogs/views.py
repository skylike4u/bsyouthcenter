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
