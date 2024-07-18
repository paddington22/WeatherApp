from django.urls import path
from .views import HomepageTemplateView, QueryHistoryTemplateView

urlpatterns = [
    path("", HomepageTemplateView.as_view(), name='homepage'),
    path('history/', QueryHistoryTemplateView.as_view(), name='query-history')
]