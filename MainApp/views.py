from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def home(request):
    # text = """
    # <h1>"Изучаем django"</h1>
    # <strong>Автор</strong>: <i>Чунин А.А.</i>
    # """
    # return HttpResponse(text)
    return render(request, "index.html")

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

def get_item(request, item_id):
    for item in items:
        if item['id'] == item_id:
            result = f"""
            <h2> Название: {item["name"]} </h2>
            <p> Количество: {item["quantity"]} </p>
            <p> <a href="/items"> Назад к списку товаров </a></p>
            """
            return HttpResponse(result)
    return HttpResponseNotFound(f"Товар с id={item_id} не найден")

def items_list(request):
    result = "<h1> Список товаров: </h1><ol>"
    for item in items:
        result += f"""<li><a href="/item/{item['id']}"> {item['name']} </li>"""
    result += "</ol>"
    return HttpResponse(result)