import numbers

from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from urlsAndViews.departments.models import Department


# Create your views here.
def index(request):
    url = reverse(numbers)
    return HttpResponse("<h1>Hello, world!</h1>")


def view_with_name(request, variable):  # Should be named the same as un urls
    # return HttpResponse(f"<h1>Variable: {variable}</h1>")
    return render(request, 'departments/name_template.html', {"variable": variable})


def view_with_args_and_kwargs(request, *args, **kwargs):
    return HttpResponse(f"<h1>Args: {args}, Kwargs: {kwargs}</h1>")


def view_with_int_pk(request, pk):
    # return HttpResponse({pk:pk}, content_type="application/json")
    return JsonResponse({"pk": pk})

def view_custom_foofo(request):
    raise Http404
def view_with_slug(request, slug):
    # OPTION 1 for 404
    # departments = Department.objects.filter(slug=slug)
    # if not departments:
    #     raise Http404

    # OPTION 2 for 404
    department = get_object_or_404(Department, slug=slug)

    # return HttpResponse(f"<h1>Department from slug: {departments}</h1>")
    raise Http404

def show_archive(request, archive_year):
    return HttpResponse(f"<h1>The year is: {archive_year}</h1>")


def redirect_to_softuni(request):
    return redirect('https://softuni.bg')


def redirect_to_view(request):
    # redirect('http://localhost:8000/numbers/')  breaks abstraction
    # redirect(index)   # breaks SR if view is from another app
    return redirect('numbers', pk=2)  # Best option

