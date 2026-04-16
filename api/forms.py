from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'university_name',
            'course_number',
            'course_name',
            'semester',
            'class_section',
            'instructor_name',
            'date_of_lecture',
            'title',
            'description',
            'notes_file'
        ]
        widgets = {
            'date_of_lecture': forms.DateInput(attrs={'type': 'date'}),
        }
