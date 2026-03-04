from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    # User relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    # Required Fields
    university_name = models.CharField(max_length=255)
    course_number = models.CharField(max_length=50)
    course_name = models.CharField(max_length=255)
    semester = models.CharField(max_length=50)
    class_section = models.CharField(max_length=50, blank=True, null=True)
    instructor_name = models.CharField(max_length=255)
    lecture_number = models.IntegerField(blank=True, null=True)
    date_of_lecture = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    # File handling
    notes_file = models.FileField(upload_to='notes/')

    # Optional / System fields
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.course_number}"