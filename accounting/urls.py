from rest_framework.routers import DefaultRouter
from .views import (
    AccountViewSet,
    CustomerViewSet,
    SupplierViewSet,
    ProductViewSet,
    TransactionViewSet,
)

router = DefaultRouter()
router.register(r'accounts', AccountViewSet, basename='account')
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'suppliers', SupplierViewSet, basename='supplier')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns = router.urls
