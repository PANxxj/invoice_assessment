from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, InvoiceDetailViewSet

router = DefaultRouter()
router.register('invoices', InvoiceViewSet,basename='invoices')
router.register('invoice-details', InvoiceDetailViewSet,basename='invoice-details')

urlpatterns = [
    path('', include(router.urls)),
]

