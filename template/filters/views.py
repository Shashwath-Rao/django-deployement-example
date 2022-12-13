from django.shortcuts import render
from django.views.generic import View
# Create your views here.
def index(request):
    """
    index page
    """
    cont={"name":"Hello world","number":100}
    return render(request,"index.html",cont)

def other(request):
    return render(request,"other.html")

class Cbview(View):
    def get(self,request):
        return render(request,"relative.html")
