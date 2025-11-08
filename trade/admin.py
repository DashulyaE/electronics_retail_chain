from django.contrib import admin
from django.utils.html import format_html

from trade.models import LinkNetwork, Contact, Product


@admin.action(description='Очистить задолженность перед поставщиком')
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)

@admin.register(LinkNetwork)
class LinkNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'get_supplier_link', 'get_level', 'debt')
    list_filter = ('contact__city',)
    actions = [clear_debt]

    def get_supplier_link(self, obj):
        if obj.supplier:
            url = f'/admin/trade/linknetwork/{obj.supplier.id}/'
            return format_html('<a href="{}">{}</a>', url, obj.supplier.name)
        return '-'

    get_supplier_link.short_description = 'Поставщик'

    def get_level(self, obj):
        return obj.get_level
    get_level.short_description = 'Уровень'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'city', 'country')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')