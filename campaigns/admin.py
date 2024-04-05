from csvexport.actions import csvexport
from django.contrib import admin
from django_tuieditor.widgets import MarkdownEditorWidget
from markdownfield.models import MarkdownField

from campaigns.models import Campaign, Petition, PetitionSignature


class CampaignAdmin(admin.ModelAdmin):
    class Media:
        css = {"all": ("css/tui-editor.css",)}

    readonly_fields = ["wordpress_id"]
    formfield_overrides = {MarkdownField: {"widget": MarkdownEditorWidget}}
    autocomplete_fields = ["events"]


class PetitionAdmin(admin.ModelAdmin):
    pass


class PetitionSignatureAdmin(admin.ModelAdmin):
    actions = [csvexport]
    list_display = [
        "get_name",
        "email",
        "zip_code",
        "created_at",
        "has_comment",
        "visible",
        "get_petition",
    ]
    list_filter = ["petition", "visible", "zip_code"]
    ordering = ["-created_at"]
    search_fields = ["first_name", "last_name", "comment", "email", "zip_code"]
    readonly_fields = [
        "first_name",
        "last_name",
        "email",
        "postal_address_line_1",
        "postal_address_line_2",
        "city",
        "state",
        "zip_code",
        "comment",
        "petition",
        "created_at",
    ]

    csvexport_selected_fields = [
        "first_name",
        "last_name",
        "email",
        "postal_address_line_1",
        "postal_address_line_2",
        "city",
        "state",
        "zip_code",
        "comment",
        "petition.title",
    ]

    def get_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    get_name.short_description = "Name"

    def get_petition(self, obj):
        return str(obj.petition)[:37] + "..." if len(str(obj.petition)) > 37 else ""

    get_petition.short_description = "Petition"

    def has_comment(self, obj):
        return bool(obj.comment)

    has_comment.boolean = True


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Petition, PetitionAdmin)
admin.site.register(PetitionSignature, PetitionSignatureAdmin)
