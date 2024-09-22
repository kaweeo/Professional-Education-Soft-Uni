from django.http import HttpResponse
from django.shortcuts import render

from urlsAndViews.departments.models import Department


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, world!</h1>")


def view_with_name(request, variable):  # Should be named the same as un urls
    return HttpResponse(f"<h1>Variable: {variable}</h1>")


def view_with_args_and_kwargs(request, *args, **kwargs):
    return HttpResponse(f"<h1>Args: {args}, Kwargs: {kwargs}</h1>")


def view_with_int_pk(request, pk):
    return HttpResponse(f"<h1>Int pk with pk: {pk}</h1>")


def view_with_slug(request, slug):
    departments = Department.objects.get(slug=slug)
    return HttpResponse(f"<h1>Department from slug: {departments}</h1>")