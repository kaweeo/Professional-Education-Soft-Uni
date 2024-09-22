from django.urls import path
from urlsAndViews.departments import views
from urlsAndViews.departments.views import index

urlpatterns = [
    path('home/', index, name='index'),
    path('<int:pk>/', views.view_with_int_pk),
    path('<slug:slug>/', views.view_with_slug),
    path('<variable>/', views.view_with_name),   # matches untill slash
    path('<path:variable>/', views.view_with_name),  # matches after the / as well "/dfgsdfsg/dfgsdg/dfgsdg/"
    # path ('<uuid:id>', some_view),
]
