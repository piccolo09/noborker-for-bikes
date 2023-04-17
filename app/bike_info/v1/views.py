from .serializers import VehicleCategorySerializer, VehicleManufacturerSerializer, VehicleModelSerializer, VehicleVariantSerializer, VehicleListingSerializer
from ..models import VehicleCategory, VehicleManufacturer, VehicleModel, VehicleVariant, VehicleListing
from rest_framework import generics,viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
class CategoryListApiView(viewsets.ReadOnlyModelViewSet):
    queryset = VehicleCategory.objects.all()
    serializer_class = VehicleCategorySerializer
    # lookup_field = "slug"

class VehicleManufacturerListApiView(viewsets.ReadOnlyModelViewSet):
    queryset = VehicleManufacturer.objects.all()
    serializer_class = VehicleManufacturerSerializer
    # lookup_field = "slug"

class VehicleModelListApiView(viewsets.ReadOnlyModelViewSet):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleModelSerializer
    # lookup_field = "slug"

class VehicleVariantListApiView(viewsets.ReadOnlyModelViewSet):
    queryset = VehicleVariant.objects.all()
    serializer_class = VehicleVariantSerializer
    # lookup_field = "slug"

class VehicleListingApiView(viewsets.ReadOnlyModelViewSet):
    queryset = VehicleListing.objects.all()
    serializer_class = VehicleListingSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('variant', 'variant__model','variant__brand',"")
    ordering_fields = ['day_rent', 'available_after']
    # lookup_field = "slug"