from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django.contrib import admin
from django.urls import include, path

schema_view = get_schema_view(
    openapi.Info(
        title="bike_rental_backend",
        default_version="v0.0.1",
        description="API Spec Documentation",
        terms_of_service="/usr/dev/null",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="No License"),
    ),
    public=True,
)


urlpatterns = [
    path(
        "",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("", include("djoser.urls.base")),
    path("v1/", include("bike_info.v1.urls")),
    path("manage/", admin.site.urls),
    path("", include("djoser.urls.jwt")),
]
