from django.contrib import admin
from django.utils.translation import ugettext as _

from genericadmin.admin import GenericAdminModelAdmin

# from . import settings
from .models import Redirect


class RedirectAdmin(GenericAdminModelAdmin):
    """The admin class for Redirect."""
    fieldsets = (
        (
            None, {
                'fields': ('site', 'from_url')
            }
        ),
        (
            _('Destination'), {
                'fields': (('content_type', 'object_id'), 'to_url'),
                'description': """Please either select a content object to which to be redirected <strong>or</strong>
                                specify a URL.""",
            }
        ),
    )

    list_display = ('from_url', 'final_destination', 'site', 'content_object', 'to_url')
    list_filter = ('site', 'content_type')
    search_fields = ('from_url', 'to_url', 'object_id')
    ordering = ('from_url',)

    def final_destination(self, instance):
        """Show the redirect's final destination URL."""
        html = None

        if instance.content_object:
            html = instance.get_content_object_url()
        elif instance.to_url:
            html = instance.to_url

        if html:
            return html
        else:
            return ''
    final_destination.allow_tags = True
    final_destination.short_description = _('Final Destination')

    # # Generic admin attributes
    # content_type_blacklist = ('auth/group', 'auth/user',)
    # content_type_lookups = settings.CONTENT_TYPE_LOOKUPS

admin.site.register(Redirect, RedirectAdmin)
