from django.urls import path

from pages.views import ContactCreateView, AboutView, HomeView, LoginView, RegisterView
from products.views import add_to_wishlist

app_name = 'contact'

urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('blog/', AboutView.as_view(), name='blog'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('wishlist/<int:pk>/', add_to_wishlist, name='add-wishlist'),
    path('', HomeView.as_view(), name='home')
]