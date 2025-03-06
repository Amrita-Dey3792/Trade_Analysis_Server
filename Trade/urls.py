from django.urls import path
from .views import TradeDataView

urlpatterns = [
    path('trades/', TradeDataView.as_view()),
    path('trades/<int:pk>/', TradeDataView.as_view()),
]
