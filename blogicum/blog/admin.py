from django.contrib import admin

from .models import Location, Category, Comment, Post


admin.site.empty_value_display = 'Планета Земля'


class PostInLine(admin.StackedInline):
    model = Post
    extra = 0


@admin.register(Category)
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


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'post',
        'author',
        'created_at',
    )
    list_editable = (
        'author',
    )
    search_fields = ('author',)
    list_filter = (
        'author',
        'created_at',
    )


@admin.register(Location)
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


@admin.register(Post)
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
