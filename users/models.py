from django.db import models
from django.contrib.auth.models import AbstractUser

class BlogUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Blog Users"

    def __str__(self):
        return f"{self.username} - {self.first_name} {self.last_name} - {self.email}"
