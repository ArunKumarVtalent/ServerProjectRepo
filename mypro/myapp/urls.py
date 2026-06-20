from django.urls import path
from .views import HomeView, CreateView, EditView, DeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', CreateView.as_view(), name='create'),
    path('edit/<int:empid>', EditView.as_view(), name='edit'),
    path('delete/<int:empid>', DeleteView.as_view(), name='delete')
]