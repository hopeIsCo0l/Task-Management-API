from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    # Defining priority choices as a class attribute
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]

    # Defining status choices
    PENDING = 'Pending'
    COMPLETED = 'Completed'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
    ]

    # Model fields
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    priority_level = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default=LOW)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default=PENDING)
    owner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)

    completed_at = models.DateTimeField(null=True, blank=True)  # Timestamp for task completion

    def mark_complete(self):
        self.status = 'Completed'
        self.completed_at = timezone.now()
        self.save()

    def mark_incomplete(self):
        self.status = 'Pending'
        self.completed_at = None
        self.save()


    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"
