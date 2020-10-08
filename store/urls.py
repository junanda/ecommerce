from django.urls import path
from .views import product, checkout, cart, updateItem, processOrder

urlpatterns = [
    path('', product, name='product'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),

    path('updateItem/', updateItem, name='updateitem'),
    path('process_order/', processOrder, name='process_order'),
]