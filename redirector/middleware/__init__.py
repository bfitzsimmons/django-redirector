import urlparse

from django.conf import settings
from django.http import HttpResponseGone, HttpResponsePermanentRedirect

from ..models import Redirect


class RedirectMiddleware(object):
    def process_response(self, request, response):
        if response.status_code != 404:
            return response

        url = request.get_full_path()
        url_qs = ''

        try:
            r = Redirect.objects.get(site__id__exact=settings.SITE_ID, url=url)
        except Redirect.DoesNotExist:
            try:
                parsed = urlparse.urlparse(url)
                r = Redirect.objects.get(site__id__exact=settings.SITE_ID, url=parsed.path)
                url_qs = parsed.query
            except (Redirect.DoesNotExist, AttributeError, TypeError):
                r = None

        if r is None and settings.APPEND_SLASH:
            # Try removing the trailing slash.
            try:
                r = Redirect.objects.get(site__id__exact=settings.SITE_ID,
                                        url=url[:url.rfind('/')] + url[url.rfind('/') + 1:])
            except Redirect.DoesNotExist:
                pass

        if r is not None:
            if not r.parent:
                return HttpResponseGone()

            # Get the top most parent record.
            if not r.is_root_node:
                root_node = r.get_root()

            # Get the `url`.
            url = root_node.url

            np = urlparse.urlparse(url)
            new_qs = ((np.query and url_qs) and '?{0}&{1}'.format(np.query, url_qs)) or \
                     (np.query and '?{0}'.format(np.query)) or \
                     (url_qs and '?{0}'.format(url_qs)) or \
                     ''

            if np.netloc:
                url = '{0}://{1}/{2}{3}'.format(np.scheme, np.netloc, np.path, new_qs)
            else:
                '{0}{1}'.format(np.path, new_qs)

            return HttpResponsePermanentRedirect(url)

        # No redirect was found. Return the response.
        return response
