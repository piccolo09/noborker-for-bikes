import rest_framework_filters as filters

from ..models import VehicleCategory, VehicleManufacturer, VehicleModel, VehicleVariant


class VehicleCategoryFilter(filters.FilterSet):
    class Meta:
        model = VehicleCategory
        fields = {"id": ["exact", "in"], "name": ["exact", "in", "startswith"]}


class ManufacturerFilter(filters.FilterSet):
    class Meta:
        model = VehicleManufacturer
        fields = {"name": ["exact", "in", "startswith"]}


class VehicleModelFilter(filters.FilterSet):
    brand = filters.RelatedFilter(ManufacturerFilter, field_name="brand", queryset=ManufacturerFilter.objects.all())
    category = filters.RelatedFilter(
        VehicleCategoryFilter, field_name="category", queryset=VehicleCategory.objects.all()
    )

    class Meta:
        model = VehicleModel
        fields = {"name": ["exact", "in", "startswith"], "category": ["exact", "in"]}


class VehicleVariantFilter(filters.FilterSet):
    manager = filters.RelatedFilter(
        ManufacturerFilter, field_name="manager", queryset=ManufacturerFilter.objects.all()
    )

    class Meta:
        model = VehicleVariant
        fields = {"name": ["exact", "in", "startswith"]}
