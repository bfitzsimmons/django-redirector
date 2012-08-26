from django.conf import settings

#######################################################################
## Generic Admin settings.
# Default content type lookups for generic admin
DEFAULT_CONTENT_LOOKUPS = getattr(settings, 'DEFAULT_CONTENT_LOOKUPS', {})
CONTENT_TYPE_LOOKUPS = getattr(settings, 'CONTENT_TYPE_LOOKUPS', {})
#######################################################################
