from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'api/v1/posts/(?P<id>\d+)/comments', CommentViewSet)
router.register('api/v1/posts', PostViewSet)

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
