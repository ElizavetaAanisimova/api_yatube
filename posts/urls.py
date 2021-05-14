from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, PostViewSet

v1_router = DefaultRouter()
v1_router.register(
    r'posts/(?P<id>\d+)/comments',
    CommentViewSet,
    basename='Comment'
)
v1_router.register(
    'posts',
    PostViewSet,
    basename='Post'
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(v1_router.urls)),
]
