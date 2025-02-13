from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


class PageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'url')  # Fields displayed in admin list




admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile)

# Register your models here.
