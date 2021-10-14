# from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView
# from Order.api.serializers import OrderSerializer, OrderItemSerializer
# from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
# from rest_framework.views import APIView
# from Order.models import Order

# class OrderCreateAPIView(CreateAPIView):
#     serializer_class = OrderSerializer
#     permission_classes = (IsAdminUser,)

#     def perform_create(self, serializer):
#         serializer.save(created_by=self.request.user)

# class OrderItemListAPIView(ListAPIView):
#     serializer_class = OrderItemSerializer
#     permission_classes = (IsAdminUser,)
#     queryset = OrderItem.objects.filter(is_active=True)

#     def list(self, request):
#         queryset = self.get_queryset()
#         serializer = OrderItemSerializer(queryset, many=True)
#         return Response(serializer.data)