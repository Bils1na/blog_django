from django.db import models
from django.conf import settings

class Post(models.Model):
    """User posts"""

    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        """Returns string info about posts"""
        return f"""{self.title}: {self.message}..."""
