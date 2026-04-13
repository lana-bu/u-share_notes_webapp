# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from .serializers import PostSerializer, UserRegistrationSerializer


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

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Guests can read, users can post

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['semester', 'instructor_name']
    search_fields = ['course_number', 'title', 'instructor_name']

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the post owner
        serializer.save(user=self.request.user)

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User account is created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # Authenticate using the email
        user = authenticate(username=email, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            # Invalid credentials
            return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutView(APIView):
    def post(self, request):
        # Log out by deleting the user's token
        if request.user.is_authenticated:
            request.user.auth_token.delete()
            return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
        return Response({"error": "You are not logged in."}, status=status.HTTP_400_BAD_REQUEST)