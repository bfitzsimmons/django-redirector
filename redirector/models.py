from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext as _

from mptt.models import MPTTModel, TreeForeignKey


class Redirect(MPTTModel):
    site = models.ForeignKey(Site, verbose_name=_('Site'), related_name='redirect_site', db_index=True)
    url = models.CharField(_('URL'), max_length=200, blank=True, db_index=True)

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['url']

    class Meta(MPTTModel.Meta):
        verbose_name = _('Redirect')
        verbose_name_plural = _('Redirects')

        unique_together = ('site', 'url')
        ordering = ('tree_id', 'lft')

    def __unicode__(self):
        return self.url
