from django.urls import path
from . import views
from . views import PostListView , PostDetailView , CreatePostView , UpdatePostView , DeletePostView
urlpatterns = [
    path('', PostListView.as_view() , name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view() , name='post-detail'),
    path('post/new/', CreatePostView.as_view() , name='post-create'),
    path('post/<int:pk>/update/', UpdatePostView.as_view() , name='post-update'),
    path('post/<int:pk>/delete/', DeletePostView.as_view() , name='post-delete'),
    path('about/', views.about , name='blog-about'),
]