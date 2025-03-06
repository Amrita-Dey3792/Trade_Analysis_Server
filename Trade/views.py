from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TradeData
from .serializers import TradeDataSerializer
from rest_framework import status

# Create your views here.
class TradeDataView(APIView):

    def get(self, request, pk=None):
        if pk:
            # Fetch trade data for a specific trade ID
            trade_data = TradeData.objects.filter(pk=pk).first()
            if not trade_data:
                return Response({"message": "Trade data not found."})
            serializer = TradeDataSerializer(trade_data)
            return Response(serializer.data)
        else:
            # Fetch all trade data
            trade_data = TradeData.objects.all()
            serializer = TradeDataSerializer(trade_data, many=True)
            return Response(serializer.data)
        
    
    def post(request):
        # Create a new trade data
        print(request.data)
        print(type(request.data))
        serializer = TradeDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def put(self, request, pk=None):
        # Update trade data for a specific trade ID
        trade_data = TradeData.objects.filter(pk=pk).first()
        if not trade_data:
            return Response({"message": "Trade data not found."})
        serializer = TradeDataSerializer(trade_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
    def delete(self, request, pk=None):
        if pk:
            # Delete trade data for a specific trade ID
            trade_data = TradeData.objects.filter(pk=pk).first()
            if not trade_data:
                return Response({"message": "Trade data not found."})
            trade_data.delete()
            return Response({"message": "Trade data deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "Invalid trade ID."})
            

        


            
