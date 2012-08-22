from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import Redirect


class RedirectAdmin(admin.ModelAdmin):
    """The admin class for Redirect."""
    fields = ('parent', 'site', 'url')
    list_display = ('__unicode__', 'site')
    list_filter = ('site',)
    search_fields = ('url', 'parent__url')
    raw_id_fields = ('parent',)
    ordering = ('url',)

    def parent_url(self, instance):
        """Returns the top-most parent."""
        return instance.parent.url
    parent_url.allow_tags = True
    parent_url.short_description = _('Parent URL')

admin.site.register(Redirect, RedirectAdmin)
