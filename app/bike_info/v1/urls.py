from rest_framework import routers
from .views import CategoryListApiView, VehicleManufacturerListApiView, VehicleVariantListApiView, VehicleModelListApiView, VehicleListingApiView

router = routers.SimpleRouter()
router.register('category', CategoryListApiView)
router.register('manufacturer', VehicleManufacturerListApiView)
router.register('models', VehicleModelListApiView)
router.register('variants', VehicleVariantListApiView)
router.register('listings', VehicleListingApiView)





urlpatterns = router.urls