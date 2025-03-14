from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from blog.views import PostViewSet, CommentViewSet, HomePageView

# Настройка Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="API для управления постами и комментариями",
    ),
    public=True,
)

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    # Админка Django
    path('admin/', admin.site.urls),

    # Маршруты для API
    path('api/', include(router.urls)),

    # Документация API (Swagger)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # Документация API (ReDoc)
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('', HomePageView.as_view(), name='home'), # Перенаправление на статическую страницу
]