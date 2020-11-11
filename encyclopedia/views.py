from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wikititle(request, title):
    return render(request, "encyclopedia/wiki.html", {
        "entryname": util.get_entry(title)     
    })


def search(request):
    query = request.GET['q']  # returns None if q not in GET
    if util.get_entry(query):
        return HttpResponseRedirect(reverse("wikititle ", args=(query,)))
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": [wikititle for wikititle in util.list_entries() if query.lower() in wikititle.lower()],
        
})

def newpage(request):
    return render(request, "encyclopedia/newpage.html")
