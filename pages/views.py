from django.shortcuts import get_object_or_404, render

# from .models import Page, Header

def index(request):
    #headers = Header.objects.filter(active=True,is_navbar=True)
    #main_headers = headers.filter(is_dropdown=False)
    #dropdown_headers= headers.filter(is_dropdown=True)
    context = {
        #"main_headers": main_headers,
        #"dropdown_headers":dropdown_headers,
        # "headers": headers,
    }
    return render(request,'index.html', context)

# def header_detail(request, slug):
#     header = get_object_or_404(Header, slug=slug)
#     pages = header.pages.all()
#     extras = header.ekstras.all()
#     template = header.template
#     template = "pages/{}".format(template)
#     context = {
#         "header": header,
#         "pages": pages,
#         "extras": extras,
#         "icon1": "icon",
#     }
    
#     return render(request, template, context)    


# def page_detail(request, slug):
#     page = get_object_or_404(Page, slug = slug)
#     context ={
#         "page":page,
#     }
#     return render(request, "pages/detail",context)
    
    
