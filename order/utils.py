from django.http import JsonResponse, HttpResponse


def SetCookie(request):
    response = HttpResponse('product_detail.html')
    response.set_cookie('bookname','Sherlock Holmes')
    return response
def set_cookies(request):
    product_id = request.POST.get('id_product')
    count = request.POST.get('count')
    # set_cookie(product_id, value, max_age=None, expires=None)
    print(product_id)
    # print(var)
    if request.method == "POST":
        print(request.POST)
        data = {
            "data": "Data has been POSTED!",
        }
        return JsonResponse(data)
