from django.shortcuts import render

# Create your views here.
def index(request):
    """
    index page
    """
    cont={"name":"Hello world","number":100}
    return render(request,"index.html",cont)

def other(request):
    return render(request,"other.html")

def relative(request):
    return render(request,"relative.html")
