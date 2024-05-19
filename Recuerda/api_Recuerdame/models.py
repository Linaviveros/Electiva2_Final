from django.db import models
from django.utils import timezone

class Pill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Reminder(models.Model):
    pill = models.ForeignKey(Pill, on_delete=models.CASCADE)
    reminder_time = models.DateTimeField()

    def is_time_to_take_pill(self):
        now = timezone.now()
        return now >= self.reminder_time


