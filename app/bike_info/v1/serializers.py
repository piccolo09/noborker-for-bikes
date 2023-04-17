from rest_framework import serializers

from ..models import VehicleCategory, VehicleListing, VehicleManufacturer, VehicleModel, VehicleVariant


class VehicleCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleCategory
        fields = ("name",)
        # lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'}
        # }


class VehicleCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleCategory
        fields = ("name",)
        # lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'}
        # }


class VehicleManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    _links = serializers.SerializerMethodField()

    class Meta:
        model = VehicleManufacturer
        fields = ("name", "_links", "url")
        # lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'}
        # }

    def get__links(self, obj):
        return {"AA": "BB"}


class VehicleModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleModel
        fields = ("name", "brand", "category")
        # lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'}
        # }


class VehicleVariantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleVariant
        fields = ("name", "model", "fuel_economy", "fuel_tank_capacity")
        # lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'}
        # }


class VehicleListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleListing
        fields = "__all__"
        # lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'}
        # }
