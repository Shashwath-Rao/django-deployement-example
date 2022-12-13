from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def index(request):
    """
    index page
    """
    cont={"name":"Hello world","number":100}
    return render(request,"index.html",cont)

def other(request):
    return render(request,"other.html")

class Cbview(TemplateView):
    template_name = "relative.html"
    get_context_data = lambda self : {"inject_me":"Hello","world":" world"}
