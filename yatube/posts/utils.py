from django.conf import settings
from django.core.paginator import Paginator


def paginator(
    request, model_object, posts_on_page=settings.PAGINATOR_ITEMS_ON_PAGE
):
    """Paginator"""
    paginator = Paginator(model_object, posts_on_page)
    return paginator.get_page(request.GET.get('page'))
