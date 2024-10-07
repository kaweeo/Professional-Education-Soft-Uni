# from datetime import datetime
# from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from forumApp.posts.forms import PostBaseForm, PostCreateForm, PostDeleteForm, SearchForm
from forumApp.posts.models import Post


# from forumApp.posts.forms import PersonForm


def index(request):
    context = {
        "my_form": "",
    }

    return render(request, "base.html", context)


def dashboard(request):
    form = SearchForm(request.GET)
    posts = Post.objects.all()

    if request.method == "GET":
        if form.is_valid():
            query = form.cleaned_data["query"]
            posts = posts.filter(title__icontains=query)

    context = {
        "posts": posts,
        "form": form,
    }

    return render(request, 'posts/dashboard.html', context)


def add_post(request):
    form = PostCreateForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()

            return redirect('dash')

    context = {
        "form": form,
    }

    return render(request, "posts/add-post.html", context)


def edit_post(request, pk: int):
    return HttpResponse()  # TODO: fix it


def details_page(request, pk: int):
    post = Post.objects.get(pk=pk)

    context = {
        "post": post,
    }

    return render(request, "posts/details-page.html", context)


def delete_post(request, pk: id):
    form = SearchForm(request.GET)
    posts = Post.objects.all()

    if request.method == "GET":
        if form.is_valid():
            query = form.cleaned_data["query"]
            posts = posts.filter(title__icontains=query)


    context = {
        "posts": posts,
    }

    # post = Post.objects.get(pk=pk)
    # form = PostDeleteForm(instance=post)  # we dont need: request.POST or None,
    #
    # if request.method == "POST":
    #     post.delete()
    #     return redirect('dash')
    #
    # context = {
    #     "form": form,
    #     "post": post,
    # }
    #
    return render(request, "posts/delete-template.html", context)

### LEARNING NOTES
# def index(request):
#     form = PersonForm(request.POST or None)
#
#     if request.method == 'POST':
#         print(request.POST['person_name'])
#
#     if form.is_valid():
#         print(form.cleaned_data['person_name'])
#
#     # context = {
#     #     "my_form": form,
#     # }
#     #
#     # return render(request, 'base.html', context)
#     #
#     # context = {
#     #     "current_time": datetime.now(),
#     #     "person": {
#     #         "age": 30,
#     #         "height": 185,
#     #     },
#     #     "ids": ["123123345345","sdfj1234123", "234543isdjfkls2342"],
#     #     "some_text": "hello, I am Kalin and I am a developer"
#     # }
#
#     # # # return HttpResponse("Hello, world. You're at the polls index.")
#     # return render(request, "base.html", context)
#
#     context = {
#         "my_form": PersonForm(),
#     }
#
#     return render(request, "base.html", context)
