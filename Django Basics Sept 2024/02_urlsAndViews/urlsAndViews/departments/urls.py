from django.urls import path, include
from urlsAndViews.departments import views
from urlsAndViews.departments.views import index

urlpatterns = [
    path('home/', index, name='index'),
    path('raise404/', views.view_custom_foofo),
    path('redirect-to-view/', views.redirect_to_view, name='redirect-view'),
    path('<int:pk>/', views.view_with_int_pk),

    # path('<slug:slug>/', views.view_with_slug),
    path('numbers/', include([
        path('<int:pk>/', views.view_with_int_pk, name='numbers'),
        path('<int:pk>/<slug:slug>/', views.view_with_slug),
    ])),
    path('<variable>/', views.view_with_name),  # matches until slash
    path('<path:variable>/', views.view_with_name),  # matches after the / as well "/dfgsdfsg/dfgsdg/dfgsdg/"
    # path ('<uuid:id>', some_view),

]
