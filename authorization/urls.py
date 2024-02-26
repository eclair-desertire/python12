from django.urls import path, include

from authorization.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
]
