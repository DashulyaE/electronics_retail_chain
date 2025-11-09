from rest_framework import serializers

from trade.models import Contact, LinkNetwork, Product


class ContactSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Contact"""

    class Meta:
        model = Contact
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Product"""

    class Meta:
        model = Product
        fields = "__all__"


class LinkNetworkSerializer(serializers.ModelSerializer):
    """Сериализатор для модели LinkNetwork"""

    contact = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all())
    products = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), many=True
    )
    supplier = serializers.PrimaryKeyRelatedField(
        queryset=LinkNetwork.objects.all(), allow_null=True
    )

    class Meta:
        model = LinkNetwork
        fields = "__all__"

    def validate_supplier(self, value):
        if value and self.instance and value == self.instance:
            raise serializers.ValidationError(
                "Объект не может быть поставщиком сам для себя."
            )
        return value
