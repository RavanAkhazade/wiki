from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import util


class SearchForm(forms.Form):
     task = forms.CharField()


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "field": SearchForm(),
    })


def get_entry(request, title):
    return render(request, "encyclopedia/entry.html", {
        "text": util.get_entry(title=title),
        "field": SearchForm()
    })


def search_field(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["name"]
            if task in util.list_entries():
                HttpResponseRedirect(reverse("encyclopedia/entry.html", args={"text": util.get_entry(title=task), "field": SearchForm()}))
            else:
                render(request, "encyclopedia/index.html", {
                    "entries": util.list_entries(),
                    "field": form
                })
    render(request, "index.html", {
        "entries": util.list_entries(),
        "field": SearchForm(),
    })