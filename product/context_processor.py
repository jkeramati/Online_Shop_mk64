from product.models import Category


def main_category(request):
    queryset = Category.objects.filter(parent=None)
    return {
        'main_cat': queryset
    }
