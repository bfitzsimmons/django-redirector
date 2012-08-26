from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext as _


class Redirect(models.Model):
    site = models.ForeignKey(Site, verbose_name=_('Site'), related_name='redirect_site', db_index=True)
    from_url = models.CharField(_('From URL'), max_length=200, db_index=True)
    to_url = models.CharField(_('To URL'), max_length=200, blank=True)

    content_type = models.ForeignKey(ContentType, verbose_name=_('Content Type'), blank=True, null=True)
    object_id = models.PositiveIntegerField(_('Object ID'), db_index=True, blank=True, null=True)
    content_object = generic.GenericForeignKey("content_type", "object_id")

    class Meta:
        verbose_name = _('Redirect')
        verbose_name_plural = _('Redirects')

        unique_together = ('site', 'from_url')

    def __unicode__(self):
        if self.object_id:
            return  '{0} ---> {1}'.format(self.from_url, self.content_object.get_absolute_url())
        else:
            return '{0} ---> {1}'.format(self.from_url, self.to_url)

    def clean(self):
        """Framework hook for validating an entire model."""
        # Make sure the user has specified either a content object *or* a URL.
        if not any([self.content_object, self.to_url]) or all([self.content_object, self.to_url]):
            raise ValidationError("""You must either select a content object *or* specify a URL.""")

        super(Redirect, self).clean()
