from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Post, Comment, PostLike, CommentLike

class Command(BaseCommand):
    help = 'Загружает тестовые данные в базу данных'

    def handle(self, *args, **kwargs):
        user = User.objects.create_user(username='testuser', password='testpass123')

        post = Post.objects.create(
            title='Тестовый пост',
            content='Это тестовый пост.',
            author=user
        )

        comment = Comment.objects.create(
            post=post,
            author=user,
            text='Это тестовый комментарий.'
        )

        PostLike.objects.create(post=post, user=user)

        CommentLike.objects.create(comment=comment, user=user)

        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно загружены!'))