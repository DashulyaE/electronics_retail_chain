from django.urls import include, path
from rest_framework.routers import DefaultRouter

from trade.apps import TradeConfig
from trade.views import ContactViewSet, LinkNetworkViewSet, ProductViewSet

app_name = TradeConfig.name

router = DefaultRouter()
router.register(r"contacts", ContactViewSet)
router.register(r"products", ProductViewSet)
router.register(r"linknetworks", LinkNetworkViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
