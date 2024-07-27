from django.db import models


class Project(models.Model):

    image = models.ImageField(upload_to="projects/", null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.TextField(max_length=200, null=True)

    # 언제 만들어 졌는지 field
    created_at = models.DateField(auto_now=True)

    # project명을 선택할 수 있도록 작업
    # self는 Project 자체를 의미하고, self.pk은 Project의 pk를 말한다. /
    def __str__(self):
        return f"{self.pk} : {self.title}"
