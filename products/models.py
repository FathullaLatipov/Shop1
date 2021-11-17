from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

UserModel = get_user_model()


class CategoryModel(models.Model):
    title = models.CharField(max_length=30, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class CategoryHomeModel(models.Model):
    name = models.CharField(max_length=30, verbose_name=_('name'))
    title = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, verbose_name=_('home_cat'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category home'
        verbose_name_plural = 'category home'


class ProductTagModel(models.Model):
    title = models.CharField(max_length=30, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('product tag')
        verbose_name_plural = _('product tags')


class BrandModel(models.Model):
    title = models.CharField(max_length=30, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brands')


class WidthModel(models.Model):
    width = models.CharField(max_length=20, verbose_name=_('width'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.width

    class Meta:
        verbose_name = _('width')
        verbose_name_plural = _('width')


class HeightModel(models.Model):
    height = models.CharField(max_length=20, verbose_name=_('height'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.height

    class Meta:
        verbose_name = _('height')
        verbose_name_plural = _('height')


class WeightModel(models.Model):
    weight = models.CharField(max_length=20, verbose_name=_('weight'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.weight

    class Meta:
        verbose_name = _('weight')
        verbose_name_plural = _('weight')


class ProductModel(models.Model):
    title = models.CharField(max_length=90, verbose_name=_('title'))
    image = models.ImageField(upload_to='products', verbose_name=_('image'))
    price = models.DecimalField(max_digits=9, decimal_places=3, verbose_name=_('price'))
    sku = models.IntegerField(verbose_name=_('sku'))
    discount = models.PositiveIntegerField(default=0, verbose_name=_('discount'))
    real_price = models.DecimalField(verbose_name=_('real price'), default=0, decimal_places=3, max_digits=9, )
    short_description = models.TextField(verbose_name=_('short_description'))
    long_description = RichTextUploadingField(verbose_name=_('long_description'))
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, related_name='products', null=True,
                                 verbose_name=_('category'), )
    brand = models.ForeignKey(BrandModel, on_delete=models.PROTECT, related_name='products', verbose_name=_('brand'))
    width = models.ForeignKey(WidthModel, on_delete=models.PROTECT, null=True, related_name='products',
                              verbose_name=_('width'))
    height = models.ForeignKey(HeightModel, on_delete=models.PROTECT, null=True, related_name='products',
                               verbose_name=_('height'))
    weight = models.ForeignKey(WeightModel, on_delete=models.PROTECT, null=True, related_name='products',
                               verbose_name=_('weight'))
    tags = models.ManyToManyField(ProductTagModel, related_name='products', verbose_name=_('tags'))


    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def is_discount(self):
        return self.discount != 0

    def __str__(self):
        return self.title

    @staticmethod
    def get_from_wishlist(request):
        wishlist = request.session.get('wishlist', [])
        return ProductModel.objects.filter(pk__in=wishlist)

    @staticmethod
    def get_from_cart(request):
        cart = request.session.get('cart', [])
        return ProductModel.objects.filter(pk__in=cart)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')


class CommentModel(models.Model):
    name = models.CharField(max_length=30, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    phone = models.CharField(max_length=30, null=True, blank=True, verbose_name=_('phone'))
    comment = models.TextField(verbose_name=_('comment'))

    post = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='comments', verbose_name=_('post'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return f'{self.name} | {self.post.title}'

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')


class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='images',
                                verbose_name=_('product'))
    image = models.ImageField(upload_to='products', verbose_name=_('image'))

    class Meta:
        verbose_name = _('product image')
        verbose_name_plural = _('product images')


