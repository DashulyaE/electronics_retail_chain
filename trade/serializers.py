from rest_framework import serializers

from trade.models import Contact, Product, LinkNetwork


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class LinkNetworkSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    products = ProductSerializer(many=True)
    supplier = serializers.PrimaryKeyRelatedField(queryset=LinkNetwork.objects.all(), allow_null=True)

    class Meta:
        model = LinkNetwork
        fields = '__all__'