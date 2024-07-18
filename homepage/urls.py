from django.urls import path
from .views import HomepageListView


urlpatterns = [
    path("", HomepageListView.as_view(), name='homepage'),
]