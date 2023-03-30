from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from blog.models import Post, Comment, Reply
from blog.serializers import PostSerializer, CommentSerializer, ReplySerializer


# Post
class PostListGetAPIView(APIView):
    permission_classes = []

    def get(self, _):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostListPostAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailAPIView(APIView):
    permission_classes = []

    def get_post(self, post_id):
        try:
            return Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return None

    def get(self, _, post_id):
        post = self.get_post(post_id)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)


class PostDetailPutDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_post(self, post_id):
        try:
            return Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return None

    def get(self, request, post_id):
        post = self.get_post(post_id)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, post_id):
        post = self.get_post(post_id)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        elif post.author.id != request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id):
        post = self.get_post(post_id)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        elif post.author.id != request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


# Comment
class CommentListPostAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_post(self, post_id):
        try:
            return Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return None

    def post(self, request, post_id):
        post = self.get_post(post_id)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(author=request.user, post=post)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailPutDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_comment(self, comment_id):
        try:
            return Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return None

    def put(self, request, post_id, comment_id):
        comment = self.get_comment(comment_id)
        if not comment:
            return Response(status=status.HTTP_404_NOT_FOUND)
        elif comment.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id, comment_id):
        comment = self.get_comment(comment_id)
        if not comment:
            return Response(status=status.HTTP_404_NOT_FOUND)
        elif comment.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


# Reply
class ReplyListPostAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_post(self, post_id):
        try:
            return Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return None

    def get_comment(self, comment_id):
        try:
            return Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return None

    def post(self, request, post_id, comment_id):
        post = self.get_post(post_id)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            comment = self.get_comment(comment_id)
            if not comment or comment.post != post:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ReplySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(author=request.user, comment=comment)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReplyDetailPutDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_reply(self, reply_id):
        try:
            return Reply.objects.get(id=reply_id)
        except Reply.DoesNotExist:
            return None

    def put(self, request, post_id, comment_id, reply_id):
        reply = self.get_reply(reply_id)
        if not reply:
            return Response(status=status.HTTP_404_NOT_FOUND)
        elif reply.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            serializer = ReplySerializer(reply, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id, comment_id, reply_id):
        reply = self.get_reply(reply_id)
        if not reply:
            return Response(status=status.HTTP_404_NOT_FOUND)
        elif reply.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            reply.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
