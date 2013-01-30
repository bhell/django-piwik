from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.sites.models import Site
from django.template import loader, Context


class Analytics(models.Model):
    site = models.OneToOneField(Site,
                                unique=True,
                                on_delete=models.CASCADE,
                                help_text=_("Django site"))
    pk_tracking_url = models.CharField(_("Tracking base URL"),
                                    max_length=255,
                                    help_text=_("URL where piwik.php is located."))
    pk_site_id = models.IntegerField(_("Piwik site ID"),
                                     help_text=_("Id of site as assigned by Piwik (see Piwik Websites page)."))

    class Meta:
        ordering = ["site",]
        verbose_name_plural = _("Analytics")

    def __unicode__(self):
        return "%s: %s" % (self.site, self.pk_tracking_url)

    @property
    def preview(self):
        t = loader.get_template('tracking_code.html')
        c = Context({'pkbaseurl': self.pk_tracking_url,
                     'pkid': self.pk_site_id})
        return t.render(c)
