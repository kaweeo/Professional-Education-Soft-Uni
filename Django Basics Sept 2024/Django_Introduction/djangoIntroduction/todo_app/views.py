from django.http import HttpResponse
from django.shortcuts import render

from djangoIntroduction.todo_app.models import Task


def index(request):
    tasks = Task.objects.all()

    # result = [
    #     '<h1>T A S K S</h1>',
    #     '<ul>',
    #     *[f"<li>{task.name}</li>" for task in tasks],
    #     '</ul>',
    # ]
    context = {
        'tasks': tasks,
    }

    # return HttpResponse('\n'.join(result))  # MIME TYPE text/html
    return render(request, 'tasks/index.html', context)
