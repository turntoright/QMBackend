import json
from rest_framework.request import Request
from . import QuoteStatus
from .models import Quote, QuoteItem
from decimal import Decimal

def create_quote(request: Request, items, quoteStatus=QuoteStatus.DRAFT):
    quote = Quote(
        quote_number=request.data['quote_number'],
        customer_id=request.data['customer_id'],
        expiry_date=request.data['expiry_date'],
        reference=request.data['reference'],
        title=request.data['title'],
        summary=request.data['summary'],
        terms=request.data['terms'],
        # status=request.data['status'],
        # amount=request.data['amount']
    )
    quote.save()
    if items is not None:
        quote.amount = create_quote_items_and_get_amount(request, items, quote)
        quote.save()
    return quote

def create_quote_items_and_get_amount(request, items, quote: Quote):
    amount = 0
    for item in items:
        amount += Decimal(item['amount'])
        quoteItem = QuoteItem(
            quote=quote,
            item_code=item['item_code'],
            description=item['description'],
            quantity=item['quantity'],
            unit_price=item['unit_price'],
            disc=item['disc'],
            tax_rate=item['tax_rate'],
            amount=item['amount']
        )
        quoteItem.save()
    return amount

