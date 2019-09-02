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
from graphene_django.views import GraphQLView
from .settings import MEDIA_URL, MEDIA_ROOT, DEBUG

favicon_view = RedirectView.as_view(url='/static/images/favicon.ico', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blogs/', include('blogs.urls')),
    path('graphql', GraphQLView.as_view(graphiql=True)),
    re_path(r'^favicon\.ico$', favicon_view),
]

if DEBUG:
    import debug_toolbar
    from rest_framework_swagger.views import get_swagger_view
    from rest_framework.documentation import include_docs_urls
    from rest_framework.schemas import get_schema_view

    schema_view = get_swagger_view(title='Vuejs_app API')
    drf_schema_view = get_schema_view(title='Vuejs_app API')

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
    urlpatterns = [
        url(r'^api-docs/$', schema_view),
        path('__debug__/', include(debug_toolbar.urls)),
        path('schema/', drf_schema_view),
        path('docs/', include_docs_urls(title='Vuejs_app API DRF')),
        path('api-auth/', include('rest_framework.urls')),  # login/logout for Browsable API

    ] + urlpatterns
