from django.urls import path
from blog.views import (
    PostListGetAPIView,
    PostListPostAPIView,
    PostDetailAPIView,
    CommentListPostAPIView,
    ReplyListPostAPIView,
    PostDetailPutDeleteAPIView,
    CommentDetailPutDeleteAPIView,
    ReplyDetailPutDeleteAPIView,
)

urlpatterns = [
    path("", PostListGetAPIView.as_view()),
    path("post/new/", PostListPostAPIView.as_view()),
    path("post/<int:post_id>/", PostDetailPutDeleteAPIView.as_view()),
    path("post/<int:post_id>/view", PostDetailAPIView.as_view()),
    path("post/<int:post_id>/comment/new/", CommentListPostAPIView.as_view()),
    path(
        "post/<int:post_id>/comment/<int:comment_id>/reply/new/",
        ReplyListPostAPIView.as_view(),
    ),
    path(
        "post/<int:post_id>/comment/<int:comment_id>/",
        CommentDetailPutDeleteAPIView.as_view(),
    ),
    path(
        "post/<int:post_id>/comment/<int:comment_id>/reply/<int:reply_id>/",
        ReplyDetailPutDeleteAPIView.as_view(),
    ),
]
