from rest_framework import routers

from .views import (
    CategoryListApiView,
    VehicleListingApiView,
    VehicleManufacturerListApiView,
    VehicleModelListApiView,
    VehicleVariantListApiView,
)

router = routers.SimpleRouter()
router.register("category", CategoryListApiView)
router.register("manufacturer", VehicleManufacturerListApiView)
router.register("models", VehicleModelListApiView)
router.register("variants", VehicleVariantListApiView)
router.register("listings", VehicleListingApiView)


urlpatterns = router.urls
