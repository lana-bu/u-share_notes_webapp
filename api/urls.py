from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import homepage, PostViewSet, UserRegistrationView, UserLoginView, UserLogoutView

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', homepage, name='homepage'),
    path('api/', include(router.urls)),
    path('signup/', UserRegistrationView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]