

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include("posts.urls")),
    
    # Third party API calls
    path('api/v1/cryptonews/', include('cryptonews.urls')),
    path('api/v1/coins/', include('coingecko.urls')),
    
    # Authentication
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    
    # Documentation
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc",), 
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui",),
    ]
