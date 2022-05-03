from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'

class Tag(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
