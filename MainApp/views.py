from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Чунин А.А.</i>
    """
    return HttpResponse(text)

author = {
    "Имя": "Антон",
    "Отчество": "Андреевич",
    "Фамилия": "Чунин",
    "телефон": "8-904-008-57-08",
    "email": "antonc89@gmail.com"
}

def about(request):
    text = f"""
    Имя: <b>{author["Имя"]}</b><br>
    Отчество: <b>{author["Отчество"]}</b><br>
    Фамилия: <b>{author['Фамилия']}</b><br>
    телефон: <b>{author['телефон']}</b><br>
    email: <b>{author['email']}</b><br>
    """
    return HttpResponse(text)

items = [
   {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
   {"id": 2, "name": "Куртка кожаная", "quantity": 2},
   {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
   {"id": 7, "name": "Картофель фри", "quantity": 0},
   {"id": 8, "name": "Кепка", "quantity": 124},
]

# def item1(request, item):
#     count_1 = 0
#     for product in items:
#         count_1 += 1
#         if product.get("id") == item:
#             return HttpResponse(f'{product.get("name"):} {product.get("quantity")} штук <br><a href="http://127.0.0.1:8000/items"> Назад к списку товаров</a>')
#         elif count_1 > len(items):
#             break
    # if item not in items:
    #     return HttpResponse(f'<h1> Товар с {product.get("id")} не найден <a href="http://127.0.0.1:8000/items"> Назад к списку товаров</a></h1>')\

def get_item(request, item_id):
    for item in items:
        if item['id'] == item_id:
            result = f"""
            <h2> Название: {item["name"]} </h2>
            <p> Количество: {item["quantity"]} </p>
            """
            return HttpResponse(result)
    return HttpResponseNotFound(f"Товар с id={item_id} не найден")