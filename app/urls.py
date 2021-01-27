from django.urls import path

from app.views import TransactionListAndCreate, TransactionUpdateAndDelete

urlpatterns = [
    path('', TransactionListAndCreate.as_view()),
    path('<int:pk>', TransactionUpdateAndDelete.as_view())
]
