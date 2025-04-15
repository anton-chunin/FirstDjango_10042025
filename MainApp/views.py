from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item

# Create your views here


# items = [
#    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
#    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
#    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
#    {"id": 7, "name": "Картофель фри", "quantity": 0},
#    {"id": 8, "name": "Кепка", "quantity": 124},
# ]


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
    item = next((item for item in items if item['id'] == item_id), None)

    if item is not None:
        context = {
            "item": item
        }
        return render(request, "item_page.html", context)
    return HttpResponseNotFound(f"Item with id={item_id} not found") 
                                
 
def get_items(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items_list.html", context)