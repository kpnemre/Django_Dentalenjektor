from django.shortcuts import get_object_or_404, render

from .models import Page


def page_detail(request, slug):
    page = get_object_or_404(Page, slug = slug)
    context ={
        "page":page,
    }
    return render(request, "pages/detail",context)
    
    
