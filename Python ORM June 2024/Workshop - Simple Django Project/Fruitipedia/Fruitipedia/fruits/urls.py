from django.urls import path, include

from . import views

urlpatterns = (
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-category/', views.create_category, name='create-category'),
    path('create-fruit/', views.CreateFruitView.as_view(), name='create-fruit'),
    path('<int:pk>/', include([
        path('edit-fruit/', views.edit_fruit, name='edit-fruit'),
        path('delete-fruit/', views.DeleteFruit.as_view(), name='delete-fruit'),
        path('details-fruit/', views.details_fruit, name='details-fruit'),
    ])),

)
