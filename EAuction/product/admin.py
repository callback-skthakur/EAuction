from django.contrib import admin
from .models import product_model

class product_admin(admin.ModelAdmin):
    list_display = ('id', 'product_name')
    list_display_links = ('id',)

admin.site.register(product_model,product_admin)
