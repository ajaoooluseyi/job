from django.db import models


class JobPosition(models.Model):
    CHOICES = (
        ('Fresher', 'Fresher'),
        ('Entry Level', 'Entry Level'),
        ('Intermediate', 'Intermediate'),
        ('Expert', 'Expert'),
    )
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    skills = models.TextField()
    experience = models.CharField(max_length=20, choices=CHOICES)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}: {self.title}"
