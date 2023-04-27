from django.shortcuts import render
from menu.models import Branch

def menu(request):
    return render(
        request,
        'base.html',
        {

        }
    )

def branch(request, title):
    parents = Branch.objects.get(title=title)
    return render(
        request,
        'branch/branch.html',
        {
            'parents': parents.title,
        }
    )