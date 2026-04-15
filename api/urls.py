from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import homepage, login_page, signup_page, create_post_page, PostViewSet, UserRegistrationView, UserLoginView, UserLogoutView

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/signup/', UserRegistrationView.as_view(), name='signup'),
    path('api/login/', UserLoginView.as_view(), name='api-login'),
    path('api/logout/', UserLogoutView.as_view(), name='logout'),
    path('', homepage, name='homepage'),
    path('login/', login_page, name='login'),
    path('signup/', signup_page, name='signup-page'),
    path('create-post/', create_post_page, name='create-post'),
]
