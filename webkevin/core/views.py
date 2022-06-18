from django.shortcuts import render, HttpResponse

html_base = """
     <h1>Mi web personal</h1>
     <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about/">Acerca de...</a></li>
        <li><a href="/portfolio/">Portafolio</a></li>
        <li><a href="/contact/">Contactos del grupo...</a></li>

     </ul>
"""

# Create your views here.
def home(request):
    return render (request, "core/home.html")
    

def about(request):
    return render (request, "core/about.html")
    


    
def contact(request):
    
    return render (request, "core/contact.html")

def base(request):
    return render (request, "core/base.html")
    
    