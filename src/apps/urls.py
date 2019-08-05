from django.urls import path, re_path

from apps import views

urlpatterns = [
    path('', views.AppsAPIList.as_view(), name='apps-API-list'),
    re_path(r'^(?P<id>[a-f0-9]{24})$', views.AppsAPIDetail.as_view(), name='apps-API-detail'),
]
