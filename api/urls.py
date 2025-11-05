
from django.urls import path, include
from api.views import sales_summary, top_customers, top_products, CustomerViewSet, OrderViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'orders', OrderViewSet, basename='order')



urlpatterns = [
    path('analytics/sales-summary/', sales_summary, name="sales-summary"),
    path('analytics/top-customers/', top_customers, name="top-customers"),
    path('analytics/top-products/', top_products, name="top-products"),
    path('', include(router.urls)),
]
