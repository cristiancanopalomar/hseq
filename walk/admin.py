from django.contrib import admin
from .models import Findings, Walks, Commitments, Supports
from django.utils.translation import ugettext, ugettext_lazy as _


class CommitmentsInline(admin.TabularInline):
    model=Commitments
    extra=0
    can_delete=False
    exclude = ('closing',)
    readonly_fields=('date',)
    raw_id_fields=('number_walk',)

class CommitmentsAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('actions and commitments'), {
            'fields': (
                    'number_walk',
                    'description',
                    'date',
                    'user_name',
                    'closing',
                )
            }),
    )
    list_display = ('number_walk', 'description', 'date', 'user_name', 'closing',)
    list_filter = ('user_name', 'date',)
    search_fields = ['number_walk', 'description', 'user_name',]
    readonly_fields = ('date',)
    raw_id_fields = ['number_walk',]


class FindingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')
    search_fields = ['description',]


class WalksAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('general information'), {
            'fields': (
                    'number_walk',
                    'creation_walks',
                    'company',
                    'activity',
                    'place',
                    'accomplished',
                    'responsible',
                )
            }),
        (_('good practices'), {
            'fields': (
                    'good_practices',
                )
            }),
        (_('characterization of the findings'), {
            'fields': (
                    'findings',
                )
            }),
        (_('description of the findings'), {
            'fields': (
                    'comments_findings',
                )
            }),
        (_('feedback and comments'), {
            'fields': (
                    'feedback_comments',
                )
            }),
        (None, {
            'fields': (
                    'image_1',
                    'image_2',
                    'image_3',
                )
            }),
    )
    list_display = ('number_walk', 'creation_walks', 'company', 'activity', 'responsible',)
    list_filter = ('responsible', 'creation_walks', 'company', 'place',)
    filter_horizontal = ('findings',)
    search_fields = ['number_walk', 'company', 'responsible', 'feedback_comments',]
    readonly_fields = ('creation_walks',)
    raw_id_fields = ['registered',]

    inlines = [CommitmentsInline,]


class SupportsAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('support commitments'), {
            'fields': (
                    'commitments',
                    'support',
                    'date',
                    'description',
                )
            }),
    )
    list_display = ('commitments', 'support', 'date', 'description',)
    list_filter = ('commitments', 'date',)
    search_fields = ['commitments', 'description',]
    readonly_fields = ('date',)
    raw_id_fields = ['commitments',]


admin.site.register(Findings, FindingsAdmin)
admin.site.register(Walks, WalksAdmin)
admin.site.register(Commitments, CommitmentsAdmin)
admin.site.register(Supports, SupportsAdmin)
