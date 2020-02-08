"""manageAppsAPIAdapter URL Configuration

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
from django.urls import path, re_path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from apps import views


@permission_classes([AllowAny])
@api_view()
def root(request):
    return Response({
                'apps': reverse('apps-API-list', request=request),               
            })

urlpatterns = [
    path('', root),
    path('admin/', admin.site.urls),
    path('api/', root),
    path('api/apps/', include(('apps.urls'))),
]
