from django.urls import path
from .views import LoginPageView, LogoutPageView, SignupPageView, PostsPageView

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login_page'),
    path('logout/', LogoutPageView.as_view(), name='logout_page'),
    path('signup/', SignupPageView.as_view(), name='signup_page'),
    path('posts/', PostsPageView.as_view(), name='posts_page'),
]
