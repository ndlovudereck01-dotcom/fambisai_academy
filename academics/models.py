from django.db import models
from django.urls import reverse

class Program(models.Model):
    LEVEL_CHOICES = [
        ('ecd', 'Early Childhood Development'),
        ('primary', 'Primary School'),
        ('senior', 'Senior School'),
    ]
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    age_range = models.CharField(max_length=50, help_text="e.g., 3-5 years")
    description = models.TextField()
    subjects = models.TextField(blank=True, help_text="Comma-separated or one per line")
    is_boarding_available = models.BooleanField(default=True)
    is_day_school_available = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"

    def get_absolute_url(self):
        return reverse('academics:program_detail', args=[self.slug])