from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_content':"Hello I'm from firstapp"}
    return render(request,'app1/index.html',context=my_dict)
