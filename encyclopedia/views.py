from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wikititle(request, title):
    return render(request, "encyclopedia/wiki.html", {
        "entry": util.get_entry(title)    
    })
