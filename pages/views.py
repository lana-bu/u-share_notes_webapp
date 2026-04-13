from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from api.models import Post

def homepage(request):
    posts = Post.objects.all().order_by('-created_at')
    home_url = reverse('home')
    return render(request, 'home.html', {'posts': posts, 'home_url': home_url})

def signup_page(request):
    signup_url = reverse('signup')
    return render(request, 'signup.html', {'signup_url': signup_url})

def create_post_page(request):
    create_post_url = reverse('create-post')
    return render(request, 'create-post.html', {'create_post_url': create_post_url})

def your_notes_page(request):
    your_notes_url = reverse('your-notes')
    return render(request, 'your-notes.html', {'your_notes_url': your_notes_url})

def post_details_page(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post_details_url = reverse('post-details', kwargs={'post_id': post.id})
    return render(request, 'post-details.html', {'post': post, 'post_details_url': post_details_url})

def profile_page(request):
    profile_url = reverse('profile')
    return render(request, 'profile.html', {'profile_url': profile_url})