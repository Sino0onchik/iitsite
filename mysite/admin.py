from django.contrib import admin
from .models import *


@admin.register(Cafedra)
class CafedraAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title', )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'is_manage')
    search_fields = ('name', )


@admin.register(CategoryPage)
class CategoryPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title', )


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title', )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name', )


@admin.register(Brands)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')


@admin.register(SiteSetting)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('address', )


@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ('current_text', 'original_text')  # Display these fields in the list view
    readonly_fields = ('original_text',)  # Prevent modification of the original text
    search_fields = ('original_text', 'current_text')  # Allow searching by both original and current text

    fieldsets = (
        (None, {
            'fields': ('original_text', 'current_text'),
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ('original_text',)
        return self.readonly_fields


class PageFilesInline(admin.TabularInline):
    model = PageFile
    extra = 1
    fields = ['file', 'description']


class PageImagesInline(admin.TabularInline):
    model = PageImage
    extra = 1
    fields = ['image']


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    inlines = [PageImagesInline, PageFilesInline]
