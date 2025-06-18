from django.contrib import admin
from .models import Address

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'district', 'is_primary')
    list_filter = ('city', 'is_primary')
    search_fields = ('user__username', 'city', 'street')
