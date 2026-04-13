from django.urls import path

from .views import homepage, about_page, create_post_page, edit_post_page, your_notes_page, post_details_page, profile_page, SignUpView

urlpatterns = [
    path('', homepage, name='home'),
    path('about/', about_page, name='about'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'), # accounts to match pattern of other user auth pages
    path('create-post/', create_post_page, name='create-post'),
    path('edit-post/<int:post_id>/', edit_post_page, name='edit-post'),
    path('your-notes/', your_notes_page, name='your-notes'),
    path('post-details/<int:post_id>/', post_details_page, name='post-details'),
]