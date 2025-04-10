from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

author = {
    "Имя": "Антон",
    "Отчество": "Андреевич",
    "Фамилия": "Чунин",
    "телефон": "8-904-008-57-08",
    "email": "antonc89@gmail.com"
}

def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Чунин А.А.</i>
    """
    return HttpResponse(text)

def about(request):
    text = f"""
    Имя: <b>{author["Имя"]}</b><br>
    Отчество: <b>{author["Отчество"]}</b><br>
    Фамилия: <b>{author['Фамилия']}</b><br>
    телефон: <b>{author['телефон']}</b><br>
    email: <b>{author['email']}</b><br>
    """
    return HttpResponse(text)