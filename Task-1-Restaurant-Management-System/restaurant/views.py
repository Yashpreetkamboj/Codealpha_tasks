from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import MenuItem, Table, Inventory, Order, Reservation
from .serializers import *

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        menu_item = serializer.validated_data['menu_item']
        quantity = serializer.validated_data['quantity']

        try:
            stock = Inventory.objects.get(item_name__iexact=menu_item.name)
            if stock.quantity < quantity:
                return Response({'error': 'Not enough inventory stock'}, status=status.HTTP_400_BAD_REQUEST)
            stock.quantity -= quantity
            stock.save()
        except Inventory.DoesNotExist:
            pass

        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        exists = Reservation.objects.filter(
            table=data['table'],
            reservation_date=data['reservation_date'],
            reservation_time=data['reservation_time']
        ).exists()
        if exists:
            return Response({'error': 'Table is already reserved at this time'}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
