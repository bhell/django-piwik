from django import template
from piwik.models import Analytics
from django.conf import settings
from django.utils.translation import ugettext as _

register = template.Library()

track = True
if settings.DEBUG:
    track = False
try:
    if not track and settings.PIWIK_IN_DEBUG == True:
        track = True
except AttributeError:
    pass

@register.inclusion_tag('tracking_code.html')
def piwik_tracking_code():
    if not track:
        error = _("Piwik not enabled in DEBUG mode. Set PIWIK_IN_DEBUG = True if really needed.")
    else:
        try:
            _site = Analytics.objects.get(site=settings.SITE_ID)
            pkbaseurl = _site.pk_tracking_url
            pkid = _site.pk_site_id
            if pkbaseurl.endswith("/piwik.php"):
                pkbaseurl = pkbaseurl.replace("/piwik.php", "/")
            elif pkbaseurl.endswith("/index.php"):
                pkbaseurl = pkbaseurl.replace("/index.php", "/")
            if not pkbaseurl.endswith("/"):
                pkbaseurl += "/"
            if pkbaseurl.startswith("http://"):
                pkbaseurl = pkbaseurl.replace("http://", "")
            elif pkbaseurl.startswith("https://"):
                pkbaseurl = pkbaseurl.replace("https://", "")
        except Analytics.DoesNotExist:
            error = _("No site found with SITE_ID %d." % settings.SITE_ID)
        except AttributeError:
            error = _("Piwik relies upon sites framework. Set up a corresponding site first to use Piwik.")
    return locals()

