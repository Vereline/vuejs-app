"""vuejs_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, re_path
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.views.decorators.csrf import csrf_exempt
from graphene_file_upload.django import FileUploadGraphQLView

from default.views import PrivateGraphQLView
from .settings import MEDIA_URL, MEDIA_ROOT, DEBUG

favicon_view = RedirectView.as_view(url='/static/images/favicon.ico', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blogs/', include('blogs.urls')),
    path('graphql', csrf_exempt(PrivateGraphQLView.as_view(graphiql=True))),
    path('file-graphql', FileUploadGraphQLView.as_view(graphiql=True)),
    # this endpoint disables graphql ui on the backend and adds csrf token protection
    # path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=False))),
    re_path(r'^favicon\.ico$', favicon_view),
]

if DEBUG:
    import debug_toolbar
    from rest_framework_swagger.views import get_swagger_view
    from rest_framework.documentation import include_docs_urls
    from rest_framework.schemas import get_schema_view

    # drf-yasg - Yet another Swagger generator
    from rest_framework import permissions
    from drf_yasg.views import get_schema_view as drf_yasg_get_schema_view
    from drf_yasg import openapi

    schema_view = get_swagger_view(title='Vuejs_app API')
    drf_schema_view = get_schema_view(title='Vuejs_app API')

    drf_yasg_schema_view = drf_yasg_get_schema_view(
        openapi.Info(
            title="Vuejs_app API",
            default_version='v1',
            description="Vuejs_app API DRF",
            terms_of_service="http://127.0.0.1:8000/docs/",
            contact=openapi.Contact(email="vstanko1998@gmail.com"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
    urlpatterns = [
        url(r'^api-docs/$', schema_view),
        # urls for drf-yasg - Yet another Swagger generator
        url(r'^drf-yasg-swagger(?P<format>\.json|\.yaml)$', drf_yasg_schema_view.without_ui(cache_timeout=0),
            name='drf-yasg-schema-json'),
        url(r'^drf-yasg-swagger/$', drf_yasg_schema_view.with_ui('swagger', cache_timeout=0),
            name='drf-yasg-schema-swagger-ui'),
        url(r'^drf-yasg-redoc/$', drf_yasg_schema_view.with_ui('redoc', cache_timeout=0),
            name='drf-yasg-schema-redoc'),

        path('__debug__/', include(debug_toolbar.urls)),
        path('schema/', drf_schema_view),
        path('docs/', include_docs_urls(title='Vuejs_app API DRF')),
        path('api-auth/', include('rest_framework.urls')),  # login/logout for Browsable API

    ] + urlpatterns
