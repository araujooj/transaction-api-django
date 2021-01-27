from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from app.models import Transaction
from app.serializers import TransactionSerializer
from functools import reduce


class TransactionListAndCreate(APIView):
    def get(self, request):
        transaction = Transaction.objects.all()
        serializer = TransactionSerializer(transaction, many=True)

        outcome_list = [item.value for item in transaction if item.type == 'outcome']
        outcome_value = reduce(lambda x, y: x + y, outcome_list, 0)

        income_list = [item.value for item in transaction if item.type == 'income']
        income_value = reduce(lambda x, y: x + y, income_list, 0)

        total = income_value - outcome_value

        return Response({
            'transactions': serializer.data,
            'wallet': {
                'income': income_value,
                'outcome': outcome_value,
                'total': total
            }})

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionUpdateAndDelete(APIView):
    def get_object(self, pk):
        try:
            return Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        serializer = TransactionSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = TransactionSerializer(self.get_object(pk), data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
