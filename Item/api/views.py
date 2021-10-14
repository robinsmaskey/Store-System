from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView
from Item.api.serializers import ItemSerializer, ItemListSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from Item.models import Item, ItemCategory
from rest_framework.response import Response

class ItemCreateAPIView(CreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ItemListAPIView(ListAPIView):
    serializer_class = ItemListSerializer
    permission_classes = (IsAdminUser,)
    queryset = Item.objects.filter(is_active=True)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ItemListSerializer(queryset, many=True)
        return Response(serializer.data)