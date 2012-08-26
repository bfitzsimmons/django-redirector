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

    list_display = ('__unicode__', 'content_object', 'to_url', 'site')
    list_filter = ('site', 'content_type')
    search_fields = ('from_url', 'to_url', 'object_id')
    ordering = ('from_url',)

    # # Generic admin attributes
    # content_type_blacklist = ('auth/group', 'auth/user',)
    # content_type_lookups = settings.CONTENT_TYPE_LOOKUPS

admin.site.register(Redirect, RedirectAdmin)
