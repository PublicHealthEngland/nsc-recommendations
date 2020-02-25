from django.contrib import admin

from .models import Organisation


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):

    list_display = ("name",)
    search_fields = ("name", "policies__name")