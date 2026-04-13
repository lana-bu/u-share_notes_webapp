from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, UserRegistrationView, UserLoginView, UserLogoutView

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('signup/', UserRegistrationView.as_view(), name='api-signup'),
    path('login/', UserLoginView.as_view(), name='api-login'),
    path('logout/', UserLogoutView.as_view(), name='api-logout'),
]