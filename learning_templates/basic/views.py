from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'basic/index.html')

def other(request):
    return render(request,'basic/other.html')

def relative(request):
    return render(request,'basic/relative_url_templates.html')
