from.models import Cart,Cartitem
from.views import cart_id
def counter(request):
    item_count=0
    if 'admin' in request.path:
        return{}
    else:
        try:
            cart=Cart.objects.filter(cart_id=cart_id(request))
            cart_items=Cartitem.objects.all().filter(cart=cart[:1])
            for cart_items in cart_items:
                item_count +=cart_items.quantity
        except:
            item_count=0
    return dict(item_count=item_count)