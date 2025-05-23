# api/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1_router = DefaultRouter()
v1_router.register("posts", PostViewSet, basename="posts")
v1_router.register("groups", GroupViewSet, basename="groups")
v1_router.register("follow", FollowViewSet, basename="follow")
v1_router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments"
)

urlpatterns = [
    path("v1/", include(v1_router.urls)),
    path("v1/jwt/create/", TokenObtainPairView.as_view(), name="jwt-create"),
    path("v1/jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("v1/jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
]
