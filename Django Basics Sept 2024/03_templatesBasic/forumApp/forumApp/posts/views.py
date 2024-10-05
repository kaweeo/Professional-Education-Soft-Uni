from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from forumApp.posts.forms import PersonForm


def index(request):
    form = PersonForm(request.POST or None)

    if request.method == 'POST':
        print(request.POST['person_name'])

    if form.is_valid():
        print(form.cleaned_data['person_name'])

    # context = {
    #     "my_form": form,
    # }
    #
    # return render(request, 'base.html', context)
    #
    # context = {
    #     "current_time": datetime.now(),
    #     "person": {
    #         "age": 30,
    #         "height": 185,
    #     },
    #     "ids": ["123123345345","sdfj1234123", "234543isdjfkls2342"],
    #     "some_text": "hello, I am Kalin and I am a developer"
    # }

    # # # return HttpResponse("Hello, world. You're at the polls index.")
    # return render(request, "base.html", context)

    context = {
        "my_form": PersonForm(),
    }

    return render(request, "base.html", context)


def dashboard(request):
    context = {
        "posts": [
            {
                "title": "How to create Django project?",
                "author": "Kalin Krumov",
                "content": "It's **quite** fun to create Django project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create Django project? 1",
                "author": "Kalin Krumov",
                "content": "It's quite fun to create Django project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create Django project? 2",
                "author": "Kalin Krumov",
                "content": "It's quite fun to create Django project",
                "created_at": datetime.now(),
            },
        ]
    }

    return render(request, "posts/dashboard.html", context)