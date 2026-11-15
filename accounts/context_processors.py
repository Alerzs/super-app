from django.conf import settings

from .catalog import (
    KESHTDRIP_CATEGORIES,
    KESHTDRIP_PRODUCTS,
    KESHTDRIP_SHOP_URL,
    KESHTHAMRAH_CATEGORIES,
    KESHTHAMRAH_SERVICES,
    KESHTHAMRAH_SERVICES_URL,
    LINKED_APPS,
    SABZIFY_CATEGORIES,
    SABZIFY_PRODUCTS,
    SABZIFY_SHOP_URL,
)


def portal(request):
    return {
        "linked_apps": LINKED_APPS,
        "sabzify_categories": SABZIFY_CATEGORIES,
        "sabzify_products": SABZIFY_PRODUCTS,
        "sabzify_shop_url": SABZIFY_SHOP_URL,
        "keshtdrip_categories": KESHTDRIP_CATEGORIES,
        "keshtdrip_products": KESHTDRIP_PRODUCTS,
        "keshtdrip_shop_url": KESHTDRIP_SHOP_URL,
        "keshthamrah_categories": KESHTHAMRAH_CATEGORIES,
        "keshthamrah_services": KESHTHAMRAH_SERVICES,
        "keshthamrah_services_url": KESHTHAMRAH_SERVICES_URL,
        "site_name": settings.SITE_NAME,
    }

