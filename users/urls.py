from django.urls import path, re_path
from .views import (
    MyProviderAuthView,
    MyTokenObtainPairView,
    MyTokenRefreshView, 
    MyTokenVerifyView, 
    LogOutView,
)

urlpatterns = [
    re_path(
        r'^o/(?P<provider>\S+)/$',
        MyProviderAuthView.as_view(),
        name='provider-auth'
    ),
    path('jwt/create/', MyTokenObtainPairView.as_view()),
    path('jwt/refresh/', MyTokenRefreshView.as_view()),
    path('jwt/verify/', MyTokenVerifyView.as_view()),
    path('logout/', LogOutView.as_view()),
]
