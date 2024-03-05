from django.http import HttpResponse

def item_list(request):
    return HttpResponse("<h1>Список элементов</h1>")
def item_detail(request,pk):
                return HttpResponse("<h1>Подробно элемент</h1>")