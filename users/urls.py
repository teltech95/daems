from django.urls import path, include
from . import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('register/', views.UserSerializer.as_view(), name='sign_up'),
    path('login/', views.AuthUserLoginView.as_view(), name='login'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    #path('', include(router.urls)),
]
