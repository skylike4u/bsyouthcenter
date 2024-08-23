from django.views.generic import TemplateView
from django.urls import path


from . import views

app_name = "blogs"

# routing
urlpatterns = [
    path("list/", TemplateView.as_view(template_name="blogs/list.html"), name="list"),
]
