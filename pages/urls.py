from django.urls import path

from .views import homepage, signup_page, create_post_page, your_notes_page, post_details_page, profile_page

urlpatterns = [
    path('', homepage, name='home'),
    path('signup/', signup_page, name='signup'),
    path('create-post/', create_post_page, name='create-post'),
    path('your-notes/', your_notes_page, name='your-notes'),
    path('post-details/<int:post_id>/', post_details_page, name='post-details'),
    path('profile/', profile_page, name='profile'),
]