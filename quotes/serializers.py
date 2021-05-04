from rest_framework import serializers

from . import models


class QuoteItemSerializer(serializers.ModelSerializer):
    # quote = serializers.ReadOnlyField(source='quote.id')

    class Meta:
        model = models.QuoteItem
        fields = ['id', 'item_code', 'description', 'quantity', 'unit_price', 'disc', 'tax_rate', 'amount']


class QuoteSerializer(serializers.ModelSerializer):
    items = QuoteItemSerializer(many=True, required=False)

    class Meta:
        model = models.Quote
        fields = ['id', 'quote_number', 'customer_id', 'create_date', 'expiry_date', 'reference',
                  'title', 'summary', 'terms', 'status', 'items', 'amount']


