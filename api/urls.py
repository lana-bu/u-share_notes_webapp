from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import homepage, login_page, logout_page, signup_page, create_post_page, your_notes_page, post_details_page, profile_page, PostViewSet, UserRegistrationView, UserLoginView, UserLogoutView

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/signup/', UserRegistrationView.as_view(), name='api-signup'),
    path('api/login/', UserLoginView.as_view(), name='api-login'),
    path('api/logout/', UserLogoutView.as_view(), name='api-logout'),
    path('', homepage, name='home'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('signup/', signup_page, name='signup'),
    path('create-post/', create_post_page, name='create-post'),
    path('your-notes/', your_notes_page, name='your-notes'),
    path('post-details/<int:post_id>/', post_details_page, name='post-details'),
    path('profile/', profile_page, name='profile'),
]