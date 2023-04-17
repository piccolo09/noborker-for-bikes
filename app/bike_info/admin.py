from django.contrib import admin
from .models import VehicleCategory,VehicleManufacturer,VehicleModel,VehicleVariant, VehicleListing
# Register your models here.
@admin.register(VehicleCategory)
class VehicleCategoryAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)
    prepopulated_fields={'slug': ('name',)}


@admin.register(VehicleManufacturer)
class VehicleManufacturerAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)
    prepopulated_fields={'slug': ('name',)}


@admin.register(VehicleModel)
class VehicleModelAdmin(admin.ModelAdmin):
    list_display=('name','brand')
    search_fields=('name','brand')
    list_filter=('brand',)
    prepopulated_fields={'slug': ('name','brand')}

@admin.register(VehicleVariant)
class VehicleModelAdmin(admin.ModelAdmin):
    list_display=("name","model","brand")
    search_fields=('name','model')
    list_filter=('model__brand','model__category')
    prepopulated_fields={'slug': ('name','model')}

    def brand(self,obj):
        return obj.model.brand

@admin.register(VehicleListing)
class VehicleListingAdmin(admin.ModelAdmin):
    list_display=("name","variant",)
    search_fields=('name','variant')
    list_filter=('variant__model','variant__model',"variant__model__brand")
    prepopulated_fields={'slug': ('name',)}

    def brand(self,obj):
        return obj.model.brand

    