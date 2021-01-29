from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


choices = [
   'white', 'green', 'yellow'
]


class Todo(models.Model):
    state = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('todo-detail', kwargs={'pk': self.pk})
