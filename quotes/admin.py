from django.contrib import admin
from .models import Quote, QuoteItem, QuoteHistory

# Register your models here.
admin.site.register(Quote)
admin.site.register(QuoteItem)
admin.site.register(QuoteHistory)
