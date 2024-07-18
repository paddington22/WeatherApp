from django.urls import path

from api.views import StaticticApiView

urlpatterns = [
    path('history/', StaticticApiView.as_view(), name='api'),
]