from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)

    def __str__(self):
        return f"Entry titled {self.title} ({self.pub_date})"
