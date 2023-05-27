from django.shortcuts import render

from .models import Cart, CartItem

@login_required
def cart_view(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total': total})
