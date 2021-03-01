from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import util


class SearchForm(forms.Form):
    query = forms.CharField()


def index(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            return HttpResponseRedirect(reverse("get_entry", args=[query]))
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": SearchForm(),
    })


def get_entry(request, title):
    if not util.get_entry(title=title):
        def to_python(name):
            return name.lower()
        return render(request, "encyclopedia/results.html", {
            "form": SearchForm(),
            "entries": util.list_entries(),
            "query": to_python(title),
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "text": util.get_entry(title=title),
            "form": SearchForm(),
            "title": title
            })
