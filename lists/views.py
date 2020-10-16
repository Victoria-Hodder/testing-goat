from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView, DetailView

from lists.forms import ExistingListItemForm, ItemForm
from lists.models import Item, List


class HomePageView(FormView):
    template_name = 'lists/home.html'
    form_class = ItemForm

"""
Note from author:
Inheritance implies an "is-a" relationship, and it’s probably not meaningful to 
say that our new list view "is-a" home page view, so, best not to do this. 
"""

class NewListView(CreateView, HomePageView):

    def form_valid(self, form):
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)

class ViewAndAddToList(DetailView, CreateView):
    model = List
    template_name = 'lists/list.html'
    form_class = ExistingListItemForm

    def get_form(self):
        self.object = self.get_object()
        return self.form_class(for_list=self.object, data=self.request.POST)