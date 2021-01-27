from django.urls import path

from app.views import TransactionListAndCreate

urlpatterns = [
    path('', TransactionListAndCreate.as_view())
]
