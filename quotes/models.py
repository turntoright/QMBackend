from django.db import models
from . import QuoteStatus, QuoteAction

# Create your models here.
QUOTE_STATUS = (
    (QuoteStatus.DRAFT, "draft"),
    (QuoteStatus.SENT, "sent"),
    (QuoteStatus.DECLINED, "declined"),
    (QuoteStatus.ACCEPTED, "accepted"),
    (QuoteStatus.INVOICED, "invoiced"),
)

QUOTE_ACTION = (
    (QuoteAction.CREATE, "create"),
    (QuoteAction.EDIT, "edit"),
    (QuoteAction.SENT, "sent"),
    (QuoteAction.VIEWED, "quote viewed"),
    (QuoteAction.MESSAGE, "message"),
    (QuoteAction.NOTE, "note"),
    (QuoteAction.ACCEPTED, "accepted"),
    (QuoteAction.INVOICED, "invoiced"),
    (QuoteAction.COPIED, "copied"),
)


class Quote(models.Model):
    quote_number = models.CharField(max_length=255)
    customer_id = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(default=None, blank=True, null=True)
    reference = models.CharField(max_length=255, default=None, blank=True, null=True)
    title = models.CharField(max_length=200, default=None, blank=True, null=True)
    summary = models.CharField(max_length=3000, default=None, blank=True, null=True)
    terms = models.CharField(max_length=4000, default=None, blank=True, null=True)
    status = models.CharField(
        choices=QUOTE_STATUS,
        default=QUOTE_STATUS[0][0],
        max_length=64
    )
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=15, blank=True, null=True)


class QuoteItem(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name='items')
    item_code = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default=None, blank=True, null=True)
    quantity = models.DecimalField(default=1, max_digits=15, decimal_places=2, null=True, blank=True)
    unit_price = models.DecimalField(default=0, decimal_places=2, max_digits=15, blank=True, null=True)
    disc = models.DecimalField(default=None, decimal_places=4, max_digits=10, blank=True, null=True)
    tax_rate = models.DecimalField(default=None, decimal_places=4, max_digits=10, blank=True, null=True)
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=15)


class QuoteHistory(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    action_date = models.DateTimeField(auto_now_add=True)
    action = models.CharField(
        choices=QUOTE_ACTION,
        default=QUOTE_ACTION[0][0],
        max_length=64
    )
    user = models.CharField(max_length=255)
    note = models.CharField(max_length=3000)



