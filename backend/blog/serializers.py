from rest_framework.serializers import ModelSerializer, ReadOnlyField
from blog.models import Post, Comment, Reply


class ReplySerializer(ModelSerializer):
    author = ReadOnlyField(source="author.username")
    comment = ReadOnlyField(source="comment.id")

    class Meta:
        model = Reply
        fields = ("id", "author", "reply_text", "date_replied", "comment")


class CommentSerializer(ModelSerializer):
    author = ReadOnlyField(source="author.username")
    replies = ReplySerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = (
            "id",
            "author",
            "comment_text",
            "date_commented",
            "replies",
        )


class PostSerializer(ModelSerializer):
    author = ReadOnlyField(source="author.username")
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "image_url",
            "content",
            "date_posted",
            "author",
            "comments",
        )
