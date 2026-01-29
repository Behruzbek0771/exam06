from django.db import models
from  django.core.exceptions import ValidationError

class Courses(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    duration_weeks = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.duration_weeks <= 0:
            raise ValidationError("Duration > 0 bo‘lishi kerak")

    def delete(self, *args, **kwargs):
        if self.enrollment_set.exists():
            raise ValidationError("Bu kursga studentlar yozilgan.")
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title