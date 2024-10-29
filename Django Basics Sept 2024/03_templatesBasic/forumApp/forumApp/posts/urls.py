from xml.etree.ElementInclude import include

from django.urls import path

from forumApp.posts.views import dashboard, add_post, delete_post, details_page, edit_post, Index, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', dashboard, name='dash'),
    path('add-post/', add_post, name='add-post'),
    path('<int:pk>/delete-post/', delete_post, name='delete-post'),
    path('<int:pk>/details-post/', details_page, name='details-post'),
    path('<int:pk>/edit-post/', edit_post, name='edit-post'),
]
