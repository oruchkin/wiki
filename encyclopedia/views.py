from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util
import random
import markdown2

markdown2.markdown("*boo!*")  # or use `html = markdown_path(PATH)`
u'<p><em>boo!</em></p>\n'

from markdown2 import Markdown
markdowner = Markdown()
markdowner.convert("*boo!*")
u'<p><em>boo!</em></p>\n'
markdowner.convert("**boom!**")
u'<p><strong>boom!</strong></p>\n'


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wikititle(request, title):
    entry_contents = util.get_entry(title)
    return render(request, "encyclopedia/wiki.html", {
        "entryname": util.get_entry(title),
        "entry_exists": entry_contents is not None,
        "title": title if entry_contents is not None else "Error",
    })


def search(request):
    query = request.GET['q']  # returns None if q not in GET
    if util.get_entry(query):
        return HttpResponseRedirect(reverse("wikititle", args=(query,)))
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": [wikititle for wikititle in util.list_entries() if query.lower() in wikititle.lower()],
            
        
})

def newpage(request):
    return render(request, "encyclopedia/newpage.html", {
        'edit_mode': False,
        'edit_page_title': '',
        'edit_page_contents': ''
    })


def save_page(request, title=None):
    if request.method == 'GET':
        return HttpResponseRedirect(reverse("index"))
    else:
        assert (request.method == 'POST')
        entry_content = request.POST['entry-content']
        if not title:
            # We are saving a new page
            title = request.POST['title'] 
            if title.lower() in [entry.lower() for entry in util.list_entries()]:
                return render(request, "encyclopedia/error.html", {
                    "error_title": "saving page",
                    "error_mgessae": "An entry with that title already exists! Please change the title and try again."
                })

        filename = "entries/" + title + ".md"
        with open(filename, "w") as file:
            file.write(entry_content)
        return HttpResponseRedirect(reverse("wikititle", args=(title,)))


def edit_page(request, title):
    entry_contents = util.get_entry(title)
    if entry_contents is None:
        # Somebody came to a url for editing a  page that does not exist
        return HttpResponseRedirect(reverse("index"))

    return render(request, "encyclopedia/newpage.html", {
        'edit_mode': True,
        'edit_page_title': title,
        'edit_page_contents': entry_contents
    })


def random_page(request):
    entry_title = random.choice(util.list_entries())
    return HttpResponseRedirect(reverse("wikititle", args=(entry_title,)))
