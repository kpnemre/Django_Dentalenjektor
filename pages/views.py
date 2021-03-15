from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from .models import *
from .forms import ContactForm

# from .models import Page, Header

def index(request):
    home = Home.objects.first()
    homedetails= HomeDetail.objects.filter(active = True)
    homefooterup= HomeFooterUp.objects.filter(active = True)
    homemiddleheader = HomeMiddleHeader.objects.filter(active = True)
    #headers = Header.objects.filter(active=True,is_navbar=True)
    #main_headers = headers.filter(is_dropdown=False)
    #dropdown_headers= headers.filter(is_dropdown=True)
    context = {
        "home":home,
        "homedetails":homedetails,
        "homefooterup":homefooterup,
        "homemiddleheader":homemiddleheader,
        #"main_headers": main_headers,
        #"dropdown_headers":dropdown_headers,
        # "headers": headers,
    }
    return render(request,'index.html', context)


def contact(request):
    # contact= ContactInfo.objects.filter(active = True)
    setting= Setting.objects.first()    
    if request.method == 'POST':
        print(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Başarı bir şekilde mesajınız tarafımıza iletilmiştir. En kısa sürede sizinle iletişime geçilecektir.')
            return redirect("home")
    else:
        form = ContactForm()
    
    context = {
        "form": form,
        # "contact":contact,
        # "abouts": abouts,
        # "rentings": rentings,
        "setting":setting,
        #"active_offer": "active"
    }

    return render(request, "contact.html", context)

def about(request):
    home = Home.objects.first()
    
    context = {
        "home":home,
    }
    return render(request,'about.html', context)

def services(request):
    home = Home.objects.first()
    
    context = {
        "home":home,
    }
    return render(request,'services.html', context)

def blog(request):
    home = Home.objects.first()
    
    context = {
        "home":home,
    }
    return render(request,'blog.html', context)


















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
    
    
