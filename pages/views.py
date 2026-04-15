from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.views.decorators.http import require_POST
from api.forms import PostForm
from api.models import Post

def homepage(request):
    posts = Post.objects.all().order_by('-created_at')
    home_url = reverse('home')
    return render(request, 'home.html', {'posts': posts, 'home_url': home_url})

def about_page(request):
    about_url = reverse('about')
    return render(request, 'about.html', {'about_url': about_url})

def create_post_page(request):
    create_post_url = reverse('create-post')
    form = PostForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            form.add_error(None, 'You must be logged in to create a post.')
        elif form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('create-post')

    return render(request, 'create-post.html', {
        'create_post_url': create_post_url,
        'form': form,
    })

def edit_post_page(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    edit_post_url = reverse('edit-post', kwargs={'post_id': post.id})
    return render(request, 'edit-post.html', {'post': post, 'edit_post_url': edit_post_url})

def your_notes_page(request):
    your_notes_url = reverse('your-notes')
    posts = Post.objects.none()

    if request.user.is_authenticated:
        posts = Post.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'your-notes.html', {
        'your_notes_url': your_notes_url,
        'posts': posts,
    })

def post_details_page(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post_details_url = reverse('post-details', kwargs={'post_id': post.id})
    return render(request, 'post-details.html', {'post': post, 'post_details_url': post_details_url})

@login_required
@require_POST
def delete_post_page(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)

    if post.notes_file:
        post.notes_file.delete(save=False)

    post.delete()
    return redirect('your-notes')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
