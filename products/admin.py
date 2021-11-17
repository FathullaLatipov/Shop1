from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from products.models import ProductTagModel, BrandModel, ProductModel, CommentModel, \
    ProductImageModel, WidthModel, HeightModel, WeightModel, CategoryModel, CategoryHomeModel


class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(CategoryModel)
class CategoryModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(CategoryHomeModel)
class CategoryHomeModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'created_at']
    search_fields = ['name', 'title', 'created_at']
    list_filter = ['created_at']


@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(BrandModel)
class BrandModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(WidthModel)
class WidthModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'width', 'created_at']
    search_fields = ['width']
    list_filter = ['created_at']


@admin.register(HeightModel)
class HeightModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'height', 'created_at']
    search_fields = ['height']
    list_filter = ['created_at']


@admin.register(WeightModel)
class WeightModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'weight', 'created_at']
    search_fields = ['weight']
    list_filter = ['created_at']


class ProductImageModelAdmin(admin.TabularInline):
    model = ProductImageModel


@admin.register(ProductModel)
class ProductModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'title', 'price', 'sku', 'category', 'brand', 'title', 'created_at']
    search_fields = ['category', 'brand', 'tags', 'created_at']
    list_filter = ['title', 'created_at']
    autocomplete_fields = ['category', 'brand', 'tags', 'width', 'height', 'weight']
    readonly_fields = ['real_price']

    inlines = [ProductImageModelAdmin]


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at']
    list_filter = ['created_at']
