from django.contrib.auth.models import User
from django.db import models

from projects.models import Project


class Article(models.Model):
    # related_name은 user네임에서 article로 접근할 때 쓰는 속성이기 때문에 직관적으로 article이라고 써줌
    writer = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="article", null=True
    )
    # 어느 project에 해당되는 지 연결고리를 만들어 준다.
    project = models.ForeignKey(
        Project, on_delete=models.SET_NULL, related_name="article", null=True
    )

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to="article/", null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)

    # like = models.IntegerField(default=0)
