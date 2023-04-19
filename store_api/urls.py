from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="e-Store API",
        default_version='v1',
        description="API for online marketplaces",
        contact=openapi.Contact(email="bahodirdadajonov2004@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('user/', include('userapp.urls')),
    path('buyurtma/', include('buyurtma.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)