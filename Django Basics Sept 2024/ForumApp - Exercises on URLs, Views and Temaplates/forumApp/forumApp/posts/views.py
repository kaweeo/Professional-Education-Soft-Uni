from datetime import datetime, time
# from django.http import HttpResponse

from django.forms import modelform_factory
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import classonlymethod, method_decorator
from django.views import View
from django.views.generic import TemplateView, RedirectView, ListView, FormView, CreateView, UpdateView, DetailView, \
    DeleteView

from forumApp.decorators import measure_execution_time
from forumApp.posts.forms import PostBaseForm, PostCreateForm, PostDeleteForm, SearchForm, PostEditForm, CommentForm, \
    CommentFormSet
from forumApp.posts.mixins import TimeRestrictedMixin
from forumApp.posts.models import Post


# from forumApp.posts.forms import PersonForm


class BaseView:  # Writing own VERY basic View class
    @classonlymethod
    def as_view(cls):

        def view(request, *args, **kwargs):
            view_instance = cls()
            return view_instance.dispatch(request, *args, **kwargs)

        return view

    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            return self.get(request, *args, **kwargs)
        elif request.method == "POST":
            return self.post(request, *args, **kwargs)
        else:
            return HttpResponseNotAllowed(['GET', 'POST'])

@method_decorator(measure_execution_time, name='dispatch')
class IndexView(TimeRestrictedMixin, TemplateView):
    template_name = 'common/index.html'  # static way
    end_time = time(17, 30)
    extra_context = {
        'static_time': datetime.now()
    }  # static way

    def get_context_data(self, **kwargs):  # dynamic way
        context = super().get_context_data(**kwargs)

        context['dynamic_time'] = datetime.now()

        return context

    def get_template_names(self):  # dynamic way
        if self.request.user.is_authenticated:
            return ['common/index_logged_in.html']
        else:
            return ['common/index.html']


# class Index(View):  # Index(BaseView)
#     def get(self, request):
#         # post_form = modelform_factory(
#         #     Post,
#         #     fields=('title', 'content', 'author'),
#         # )
#         #
#         # context = {
#         #     "my_form": post_form,
#         # }
#
#         context = {
#             'dynamic_time': datetime.now()
#         }
#
#         return render(request, "common/index.html", context)


# def index(request):               # FBV
#     post_form = modelform_factory(
#         Post,
#         fields=('title', 'content', 'author'),
#     )
#
#     context = {
#         "my_form": post_form,
#     }
#
#     return render(request, "common/index.html", context)


class DashboardView(ListView, FormView):
    template_name = 'posts/dashboard.html'
    context_object_name = 'posts'
    form_class = SearchForm
    paginate_by = 1
    success_url = reverse_lazy('dash')
    model = Post

    def get_queryset(self):
        queryset = self.model.objects.all()

        if 'query' in self.request.GET:
            query = self.request.GET.get('query')
            queryset = self.queryset.filter(title__icontains=query)

        return queryset


# def dashboard(request):
#     form = SearchForm(request.GET)
#     posts = Post.objects.all()
#
#     if request.method == "GET":
#         if form.is_valid():
#             query = form.cleaned_data["query"]
#             posts = posts.filter(title__icontains=query)
#
#     context = {
#         "posts": posts,
#         "form": form,
#     }
#
#     return render(request, 'posts/dashboard.html', context)


class AddPostView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/add-post.html'
    success_url = reverse_lazy('dash')


# def add_post(request):
#     form = PostCreateForm(request.POST or None, request.FILES or None)
#
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect('dash')
#
#     context = {
#         "form": form,
#     }
#
#     return render(request, "posts/add-post.html", context)


class EditPostView(UpdateView):
    model = Post
    # form_class = PostEditForm
    template_name = 'posts/edit-post.html'
    success_url = reverse_lazy('dash')

    def get_form_class(self):
        if self.request.user.is_superuser:
            return modelform_factory(Post, fields=('title', 'content', 'author', 'languages'))
        else:
            return modelform_factory(Post, fields=('content',))


# def edit_post(request, pk: int):
#     post = Post.objects.get(pk=pk)
#
#     if request.method == "POST":
#         form = PostEditForm(request.POST, instance=post)
#
#         if form.is_valid():
#             form.save()
#             return redirect('dash')
#     else:
#         form = PostEditForm(instance=post)
#
#     context = {
#         "form": form,
#         "post": post,
#     }
#
#     return render(request, "posts/edit-post.html", context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/details-post.html'

    def get_context_data(self, **kwargs):
        print(PostDetailView.__mro__)
        context = super().get_context_data(**kwargs)
        context['formset'] = CommentFormSet()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        formset = CommentFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()
            return redirect('details-post', pk=post.id)

        context = self.get_context_data()
        context['formset'] = formset

        return self.render_to_response(context)


# def details_page(request, pk: int):
#     post = Post.objects.get(pk=pk)
#     formset = CommentFormSet(request.POST or None)
#
#     if request.method == "POST":
#         if formset.is_valid():
#             for form in formset:
#                 if form.cleaned_data:
#                     comment = form.save(commit=False)
#                     comment.post = post
#                     comment.save()
#
#             return redirect('details-post', pk=post.id)
#
#     context = {
#         "post": post,
#         "formset": formset,
#     }
#
#     return render(request, "posts/details-post.html", context)


class DeletePostView(DeleteView):
    model = Post
    form_class = PostDeleteForm
    template_name = 'posts/delete-post.html'
    # context_object_name = 'post'
    success_url = reverse_lazy('dash')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post = Post.objects.get(pk=pk)
        return post.__dict__


# def delete_post(request, pk: id):
#     # form = SearchForm(request.GET)
#     # posts = Post.objects.all()
#     #
#     # if request.method == "GET":
#     #     if form.is_valid():
#     #         query = form.cleaned_data["query"]
#     #         posts = posts.filter(title__icontains=query)
#     #
#     #
#     # context = {
#     #     "posts": posts,
#     # }
#
#     post = Post.objects.get(pk=pk)
#     form = PostDeleteForm(instance=post)  # we dont need: request.POST or None
#
#     if request.method == "POST":
#         post.delete()
#         return redirect('dash')
#
#     context = {
#         "form": form,
#         "post": post,
#     }
#
#     return render(request, "posts/delete-post.html", context)


class RedirectHomeView(RedirectView):
    url = reverse_lazy('index')  # static way

    def get_redirect_url(self, *args, **kwargs):  # dynamic way
        pass

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
