from django.shortcuts import render
import random
import string

# Create your views here.

def generate_password(length, bigLetters=False, numbers=False, specials=False):
    characters = string.ascii_lowercase # zbiór małych liter

    if bigLetters:
        characters += string.ascii_uppercase  # dodawanie dużych liter

    if numbers:
        characters += string.digits  # dodawanie liczb

    if specials:
        characters += string.punctuation  # dodawanie znaków specialnych

    password = ''.join(random.choice(characters) for _ in range(length))# losowanie znaków
    # for _ in range(length):
    #     password += random.choice(characters)

    return password

def home(request):
    return render(request, 'home.html')

def password(request):
    # print(request.POST.get('big'))
    length = int(request.POST.get('length'))
    big_letters_included = request.POST.get('big')
    numbers_included = request.POST.get('numbers')
    specials_included = request.POST.get('specials')

    password = generate_password(length,big_letters_included, numbers_included,specials_included)
    return render(request, 'password.html', {'password': password})

def about(request):
    text = "To jest krótki tekst o nas"
    return render(request, 'about.html', {'text': text})