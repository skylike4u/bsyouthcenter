from django.db import models


class Member(models.Model):
    """members definition"""

    member_list = models.CharField(max_length=100)

    def __str__(self):
        return self.member_list
