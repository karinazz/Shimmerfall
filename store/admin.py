from django.contrib import admin

# Register your models here.

from . models import Cathegory, Product


#admin.site.register(Cathegory)
#admin.site.register(Product)

@admin.register(Cathegory)
class CathegoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug' : ('name',)}



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug' : ('title',)}