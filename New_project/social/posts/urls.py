from django.urls import path

from posts import views

app_name = 'posts'


urlpatterns = [
    path("", views.PostList.as_view(), name="all"),
    path("new/", views.CreatePost.as_view(), name="create"),
    path("by/P<username>/",views.UserPosts.as_view(),name="for_user"),
    path("by/P<username>/P<pk>",views.PostDetail.as_view(),name="single"),
    path("delete/P<pk>/",views.DeletePost.as_view(),name="delete"),
]
