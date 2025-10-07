from django.shortcuts import render,HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    # context={#context is a set of variable 
    #     "variable1":"variable 1 value  ",
    #     "variable2":"variable 2 value",
    #     "variable3":"variable 3 value is "

    # }
    # return render(request,'index.html',context)
    return render(request,'index.html')

def about(request):
    # return HttpResponse("This is about  page ")
    return render(request,'about.html')

def contact(request):
    # return HttpResponse("This is nothing page ")
    #if have request and enter the form then save it in database
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        description=request.POST.get('description')
        


    return render(request,'contact.html')
