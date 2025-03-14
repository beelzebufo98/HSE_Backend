from rest_framework import viewsets
from .models import Post, Comment, PostLike, CommentLike
from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'index.html'

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        PostLike.objects.create(post=post, user=user)
        return Response({'status': 'liked'})

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        like, created = CommentLike.objects.get_or_create(comment=comment, user=user)

        if not created:
            like.delete()
            status = 'unlike'
        else:
            status = 'like'

        return Response({'status': status})