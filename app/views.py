from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from app.models import Transaction
from app.serializers import TransactionSerializer


class TransactionListAndCreate(APIView):
    def get(self, request):
        transaction = Transaction.objects.all()
        serializer = TransactionSerializer(transaction, many=True)

        return Response({
            'transactions': serializer.data,
            'wallet': {
                'income': 300,
                'outcome': 200,
                'total': 100
            }})

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
