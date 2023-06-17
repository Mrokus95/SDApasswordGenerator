from django.shortcuts import render
import random
import string

# Create your views here.


def generate_email(length, domain, numbers=False):
    characters = string.ascii_lowercase  # zbiór małych liter

    if numbers:
        characters += string.digits  # dodawanie liczb

    email = ''.join(random.choice(characters) for _ in range(length))
    email += "@" + domain

    return email


def home(request):
    return render(request, 'home2.html')


def result(request):
    text = "Twój e-mail to:"

    domain = request.POST.get('domain')
    length = int(request.POST.get('length'))
    number = request.POST.get('number')

    email = generate_email(length, domain, number)
    return render(request, 'result2.html', {'email': email, 'text': text})


def about(request):
    text = "To jest krótki tekst o generatorze e-mail"
    return render(request, 'about2.html', {'text': text})
