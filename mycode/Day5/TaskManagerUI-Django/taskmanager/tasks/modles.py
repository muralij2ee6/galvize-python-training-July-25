from django.db import models
from django.urls import reverse
from django.utils import timezone


class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    due_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['priority', 'due_date', 'created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])

    def get_priority_class(self):
        return {
            1: 'high-priority',
            2: 'medium-priority',
            3: 'low-priority',
        }.get(self.priority, '')

    def is_overdue(self):
        return self.due_date and self.due_date < timezone.now().date() and not self.completed