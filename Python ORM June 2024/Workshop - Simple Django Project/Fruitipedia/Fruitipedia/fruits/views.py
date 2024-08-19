from django.contrib.messages import success
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from .forms import CategoryAddForm, FruitAddForm, EditFruitForm, DeleteFruitForm
from .models import Fruit


# Create your views here.
def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()

    context = {
        'fruits': fruits
    }

    return render(request, 'common/dashboard.html', context)


# def create_fruit(request):
#     return render(request, 'fruits/create-fruit.html')
class CreateFruitView(CreateView):
    model = Fruit
    form_class = FruitAddForm
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('dashboard')


def details_fruit(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    context = {
        'fruit': fruit
    }

    return render(request, 'fruits/details-fruit.html', context)


def edit_fruit(request, pk):
    fruit = Fruit.objects.get(pk=pk)

    if request.method == 'GET':
        form = EditFruitForm(instance=fruit)
    else:
        form = EditFruitForm(request.POST, instance=fruit)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit
    }

    return render(request, 'fruits/edit-fruit.html', context)


# def delete_fruit(request, fruit_pk):
#     return render(request, 'fruits/delete-fruit.html')

class DeleteFruit(DeleteView):
    model = Fruit
    form_class = DeleteFruitForm
    template_name = 'fruits/delete-fruit.html'
    success_url = reverse_lazy('dashboard')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(instance=self.object)
        return self.render_to_response(self.get_context_data(form=form, object=self.object))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)


def create_category(request):
    if request.method == "GET":
        form = CategoryAddForm()
    else:  # if post
        form = CategoryAddForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        "form": form,
    }

    return render(request, 'categories/create-category.html', context)
