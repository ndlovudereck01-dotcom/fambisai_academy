from django.db import models

class ApplicationInquiry(models.Model):
    parent_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    child_name = models.CharField(max_length=200)
    child_dob = models.DateField()
    program_interest = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.parent_name} - {self.child_name}"