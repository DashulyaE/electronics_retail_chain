from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets

from .models import Contact, LinkNetwork, Product
from .serializers import (ContactSerializer, LinkNetworkSerializer,
                          ProductSerializer)


class IsActiveUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_active


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated, IsActiveUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ["city", "country"]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsActiveUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "model"]


class LinkNetworkViewSet(viewsets.ModelViewSet):
    queryset = LinkNetwork.objects.all()
    serializer_class = LinkNetworkSerializer
    permission_classes = [permissions.IsAuthenticated, IsActiveUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["contact__country"]
    search_fields = ["name", "contact__city", "contact__country"]

    def perform_update(self, serializer):
        if "debt" in serializer.validated_data:
            serializer.validated_data.pop("debt")
        serializer.save()
