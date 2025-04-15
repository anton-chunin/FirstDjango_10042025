from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    context = { 
        "name": "Петров Иван Николаевич",
        "email": "my_mail@mail.ru"
    }
    return render(request, "index.html", context)
    

def about(request):
    author = {
    "name": "Антон",
    "middle_name": "Андреевич",
    "last_name": "Чунин",
    "phone": "8-904-008-57-08",
    "email": "antonc89@gmail.com"
    }
    return render(request, "about.html", {"author": author})


def get_item(request, item_id: int):
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Item with id={item_id} not found")
    else:
        context = {"item": item}
        return render(request, "item_page.html", context)
     
                                
 
def get_items(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items_list.html", context)