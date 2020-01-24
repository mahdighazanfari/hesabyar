from django.urls import path, include

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('contact/get', views.get_contacts, name='get_contacts'),
    path('transaction/get', views.get_transactions, name='get_transactions'),
    path('transaction/new', views.add_transaction, name='add_transactions'),
    path('transaction/delete', views.delete_transaction, name='delete_transaction'),
    path('transaction/edit', views.edit_transaction, name='edit_transaction'),
    path('', views.index, name='index'),
]
