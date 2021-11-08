from django.contrib import admin

# Register your models here.
from .models import Movie, Category, Cast

#admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Cast)


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'watch_count','my_custom_display_field']
    list_display_links = ['name','watch_count']
    list_editable = ['description']
    search_fields = ['name']
    list_filter = ['category', 'rate']
    readonly_fields = ("my_custom_display_field",)
    #fields = ['name','description', ('likes', 'watch_count', 'rate'), 'category','actors', 'production_date']

    def my_custom_display_field(self,obj):
        if obj.likes and obj.watch_count:
            total = 100 * (obj.likes / obj.watch_count)
            return '{} %'.format(round(total))
        return '0'

    my_custom_display_field.short_description = 'watch/likes rating'

    fieldsets = (
        ["main", {"fields":["name", "description"]}],
        ["rate and likes..", {"fields":["likes", "watch_count", "rate","my_custom_display_field","category"]}],
        ["attachments",{"fields":["image"]}],
        ["Actors",{"fields":["actors"]}]

    )



admin.site.register(Movie,MovieAdmin)
