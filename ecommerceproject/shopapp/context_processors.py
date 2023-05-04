from.models import Category
def menu_links(request):
    links1=Category.objects.all()
    return dict(links=links1)