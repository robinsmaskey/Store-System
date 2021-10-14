from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView, RetrieveUpdateAPIView
from Shop.api.serializers import ShopSerializer, ShopListSerializer, ShopCategorySerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from Shop.models import Shop
from rest_framework.response import Response

class ShopCreateAPIView(CreateAPIView):
    serializer_class = ShopSerializer
    permission_classes = (IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ShopRetrieveAPIView(RetrieveAPIView):
    serializer_class = ShopSerializer
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = 'pk'
    queryset = Shop.objects.all()

class ShopUpdateAPIView(UpdateAPIView):
    serializer_class = ShopSerializer
    permission_classes = (IsAdminUser,)
    queryset = Shop.objects.filter(is_active=True)

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)


class ShopListAPIView(ListAPIView):
    serializer_class = ShopListSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Shop.objects.filter(is_active=True)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ShopListSerializer(queryset, many=True)
        return Response(serializer.data)
        

class ShopRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = ShopSerializer
    permission_classes = (IsAdminUser,)

       



