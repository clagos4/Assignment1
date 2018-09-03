from django.db import models

class Comment(models.Model):

    comment = models.TextField()
    author_ip = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
