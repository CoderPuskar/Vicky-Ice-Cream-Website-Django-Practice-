from django.shortcuts import render,HttpResponse

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
    return render(request,'contact.html')
