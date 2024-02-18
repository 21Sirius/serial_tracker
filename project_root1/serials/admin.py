from django.contrib import admin

from serials.models import Genre, Serial


# Register your models here.

# admin.site.register(Genre)
# admin.site.register(Serial)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Serial)
class SerialAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
