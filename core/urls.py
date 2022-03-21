from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
admin.site.site_header = "Disaster & national emergency alert admin"
admin.site.site_title = "Disaster & national emergency alert admin site"
admin.site.index_title = "Disaster & national emergency alert Admin"

schema_view = get_schema_view(
    openapi.Info(
        title="Teltech API",
        default_version='v1',
        description="This is a REST API for a {--testing--} service",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('api/', include('alerts.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('swagger<format>.json|.yaml/',
         schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('auth/', include('djoser.urls.jwt')),
]
