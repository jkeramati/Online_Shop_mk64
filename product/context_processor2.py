from order.models import CartItem


def count_basket(request):
    count = CartItem.objects.filter(cart__status='NPY').count()
    return {
        'number_basket': count
    }
