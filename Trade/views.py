from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from .models import Stock
from .serializers import StockSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

# ViewSet for Stock CRUD operations
class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['trade_code', 'date']
    pagination_class = PageNumberPagination

    @action(detail=False, methods=['get'])
    def chart_data(self, request):
        trade_code = request.query_params.get('trade_code', None)
        if trade_code:
            stocks = Stock.objects.filter(trade_code=trade_code).order_by('date')
        else:
            return Response(
                status=400,
                data={
                    'error': 'Trade code not provided.'
                }
            )
        
        data = []
        for stock in stocks:
            data.append({
                'date': stock.date.strftime('%Y-%m-%d'),
                'close': stock.close,
                'volume': stock.volume,
            })
        return Response(data)
    
    @action(detail=False, methods=['get'], url_path='unique-trade-codes')
    def unique_trade_codes(self, request):
        """
        Returns a list of unique trade codes available in the database.
        """
        trade_codes = Stock.objects.values_list('trade_code', flat=True).distinct()
        return Response(list(trade_codes))