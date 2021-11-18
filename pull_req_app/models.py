from django.db import models


# Create your models here.


class UserRequest(models.Model):
    user_link = models.URLField(verbose_name='Ссылка на публичный репозиторий', unique=True)

    def __str__(self):
        return f'{self.id}'


class UserRequestResult(models.Model):
    user_link = models.ForeignKey(UserRequest, on_delete=models.CASCADE)
    pull_request = models.CharField(max_length=255)
    pull_request_link = models.URLField()
    pull_request_reviewers = models.CharField(max_length=100, verbose_name='Reviewers (usernames)', null=True,
                                              blank=True)
    pull_request_assignees = models.CharField(max_length=100, verbose_name='Assignees (usernames)', null=True,
                                              blank=True)

    def __str__(self):
        return f'{self.user_link, self.pull_request}'
