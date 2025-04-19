from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,ProductViewSet,SaleViewSet



router = DefaultRouter()
router.register('users', UserViewSet)
router.register('products', ProductViewSet)
router.register('sales', SaleViewSet)


urlpatterns = [
    path('',include(router.urls)),
]