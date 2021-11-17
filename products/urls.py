from django.urls import path

from products.views import ProductsListView, ProductDetailView, CommentCreateView, WishlistListView, \
    CartListView, add_to_cart, add_to_wishlist

app_name = 'products'

urlpatterns = [
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('cart/', CartListView.as_view(), name='cart'),
    path('cart/<int:pk>/', add_to_cart, name='add-cart'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment'),
    path('wishlist/', WishlistListView.as_view(), name='wishlist'),
    path('wishlist/<int:pk>/', add_to_wishlist, name='add-wishlist'),
    path('', ProductsListView.as_view(), name='lists'),

]