from django.db import models
from django.core.exceptions import ValidationError

class Students(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.age < 16:
            raise ValidationError("Student 16 yoshdan katta bo'lishi kerak")

    def __str__(self):
        return self.full_name