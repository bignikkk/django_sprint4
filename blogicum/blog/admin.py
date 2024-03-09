from django.contrib import admin

from blog.models import Location, Category, Post

admin.site.empty_value_display = 'Планета Земля'


class PostInLine(admin.StackedInline):
    model = Post
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInLine,
    )
    list_display = (
        'title',
        'description',
        'slug',
        'is_published',
        'created_at',
    )
    search_fields = ('title',)
    list_filter = ('slug',)


class LocationAdmin(admin.ModelAdmin):
    inlines = (
        PostInLine,
    )
    list_display = (
        'name',
        'is_published',
        'created_at',
    )
    search_fields = ('name',)
    list_filter = ('is_published',)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'author',
        'pub_date',
        'is_published',
        'created_at',
        'category',
        'location'
    )
    list_editable = (
        'author',
        'is_published',
        'category',
        'location'
    )
    search_fields = ('title',)
    list_filter = (
        'author',
        'category',
        'location',
    )
    list_display_links = ('title',)


admin.site.register(Location, LocationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
