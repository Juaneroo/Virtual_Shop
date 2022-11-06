from django.contrib import admin
from inventario.models import Productos

# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    list_display=('name', 'cost', 'cantidad_stock', 'description')
    search_fields = ('name', 'cost', 'description')

# admin.site.register(Productos)

admin.site.register(Productos, ProductosAdmin)