from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['user_text']
    reversed_text = user_text[::-1]
    count_text = len(user_text.split())
    return render(request, 'reverse.html', {'user_text': user_text, 'reversed_text': reversed_text, 'count_text': count_text})