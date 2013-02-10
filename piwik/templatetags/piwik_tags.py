from django import template
from piwik.models import Analytics
from django.conf import settings
from django.utils.translation import ugettext as _
from decimal import Decimal

register = template.Library()

track = True
if settings.DEBUG:
    track = False
try:
    if not track and settings.PIWIK_IN_DEBUG == True:
        track = True
except AttributeError:
    pass


def _get_code():
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
    return {'error': error,
            'pkbaseurl': pkbaseurl,
            'pkid': pkid}


@register.inclusion_tag('tracking_code.html')
def piwik_tracking_code():
    context = _get_code()
    return context


@register.inclusion_tag('tracking_404.html')
def piwik_tracking_404():
    context = _get_code()
    return context


@register.inclusion_tag('tracking_order_confirm.html')
def piwik_order_confirm():
    context = _get_code()
    # order
    #   .products
    #      .sku // "9780786706211" (required) SKU: Product unique identifier
    #      .name // "Endurance: Shackleton's Incredible Voyage" (optional) Product name
    #      .categories (list) // "Adventure Books" (optional) Product category. You can also specify an array of up to 5 categories eg. ["Books", "New releases", "Biography"]
    #      .price // 8.8 (recommended) Product price
    #      .quantity // (optional, default to 1) Product quantity
    #   .id // "A10000123" (required) Unique Order ID
    #   .revenue // 35 (required) Order Revenue grand total (includes tax, shipping, and subtracted discount)
    #   .subtotal // 30 (optional) Order sub total (excludes shipping)
    #   .tax // 5.5 (optional) Tax amount
    #   .shipping // 4.5 (optional) Shipping amount
    #   .discount // (optional) Discount offered (set to false for unspecified parameter)
    return context


@register.inclusion_tag('tracking_add_to_cart.html')
def piwik_add_to_cart():
    context = _get_code()
    # product (new product, optional)
    #   .sku
    #   .name
    #   .categories (list)
    #   .price
    #   .quantity
    # cart
    #   .products (entire cart, same attributes as above)
    #   .amount // 15.5 (recommended) Cart amount
    return context


@register.inclusion_tag('tracking_product_view.html')
def piwik_product_view():
    context = _get_code()
    # EITHER
    # product (new product, optional)
    #   .sku
    #   .name
    #   .categories (list)
    #   .price
    # OR
    # categories (list of categories)
    return context


@register.inclusion_tag('tracking_goal_revenue.html')
def piwik_goal_revenue(goalid, revenue):
    """Include tracking code for goal with custom revenue.

    Arguments:
    goalid: Piwik goal ID (anything convertible to integer)
    revenue: Value to be tracked (anything convertible to decimal number)"""
    context = _get_code()
    try:
        goalid = int(goalid)
        revenue = Decimal(revenue)
    except:
        return None
    context['goalid'] = goalid
    context['revenue'] = revenue
    return context


