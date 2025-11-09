from django.contrib import admin

from trade.models import Contact, LinkNetwork, Product


@admin.action(description="Очистить задолженность перед поставщиком")
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(LinkNetwork)
class LinkNetworkAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "contact", "get_supplier_name", "get_level", "debt")
    list_filter = ("contact__city",)
    actions = [clear_debt]

    def get_supplier_name(self, obj):
        return obj.supplier.name if obj.supplier else "-"

    get_supplier_name.short_description = "Поставщик"

    def get_level(self, obj):
        return obj.get_level

    get_level.short_description = "Уровень"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "city", "country")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "model", "release_date")
