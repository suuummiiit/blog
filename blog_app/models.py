from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Deletes all the user's posts, when the user is deleted

    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)