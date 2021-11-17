from django import template
from django.db.models import Sum
from django.templatetags.static import static

from products.models import ProductModel

register = template.Library()


@register.simple_tag
def get_url_lang(request, lang):
    url = request.path
    url = url.split('/')
    url[1] = lang
    url = '/'.join(url)

    return url


@register.simple_tag
def get_price(request, x):
    price = request.GET.get('price')
    if price:
        return price.split(';')[x]
    return 'null'


# @register.simple_tag
# def get_heart_icon(request, product):
#     if request.user in product.wishlist.all():
#         return static('/img/features/like.png')
#     return static('/img/features/love.png')

@register.filter()
def in_wishlist(wishlist, request):
    return wishlist.pk in request.session.get('wishlist', [])


@register.simple_tag
def get_wishlist_count(request):
    wishlist = request.session.get('wishlist')
    if wishlist:
        return len(wishlist)
    return 0


@register.filter()
def in_wishlist(wishlist, request):
    return wishlist.pk in request.session.get('wishlist', [])


@register.simple_tag
def get_cart_count(request):
    cart = request.session.get('cart')
    if cart:
        return len(cart)
    return 0


@register.simple_tag
def get_cart_count2(request):
    cart = request.session.get('cart')
    if cart:
        return len(cart)
    return 0


@register.filter()
def in_cart(product, request):
    return product.pk in request.session.get('cart', [])


@register.simple_tag()
def get_cart_sum(request):
    cart = request.session.get('cart')
    if not cart:
        return 0

    return ProductModel.get_from_cart(request).aggregate(Sum('real_price'))['real_price__sum']


@register.simple_tag
def get_profile(request):
    if request.is_authenticated:
        return request.user.profile
