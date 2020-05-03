from django.contrib import admin

from .models import Gallery, GalleryItem


class GalleryItemInline(admin.StackedInline):
    model = GalleryItem


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryItemInline]
    list_display = ["name", 'slug']
    ordering = ["name"]
    search_fields = ["name"]


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    pass
