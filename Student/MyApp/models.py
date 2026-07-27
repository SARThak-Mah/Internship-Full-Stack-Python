from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    course = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    skills = models.CharField(max_length=255)  # Comma-separated skills

    # Restrict file extensions strictly to .jpg, .jpeg, and .png
    profile_photo = models.ImageField(
        upload_to='student_photos/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
    )
    about = models.TextField()

    def __str__(self):
        return self.full_name
