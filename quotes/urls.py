from django.urls import path

from . import views
from .views import QuoteListView, QuoteDetailView

urlpatterns = [
    path("", views.quote_req, name='quote-request'),
    path("show/<int:pk>", QuoteDetailView.as_view(), name='quote-detail'),
    path("show", QuoteListView.as_view(), name='quote-list'),
]
