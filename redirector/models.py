from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext as _


class Redirect(models.Model):
    site = models.ForeignKey(Site, verbose_name=_('Site'), related_name='redirect_site', db_index=True)
    url = models.CharField(_('URL'), max_length=200, blank=True, db_index=True)

    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = _('Redirect')
        verbose_name_plural = _('Redirects')

        unique_together = ('site', 'url')

    def __unicode__(self):
        return '{0} ---> {1}'.format(self.url, self.get_root().url)

    def get_root(self):
        node = self
        while node.parent:
            node = node.parent
        return node

    @property
    def is_root_node(self):
        if self is self.get_root():
            return True
