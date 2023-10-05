from django.shortcuts import render
from django.views import generic
from .models import Item

class MenuList(generic.ListView):
    queryset = Item

class MenuItemDetail(generic.DetailView):
    pass
