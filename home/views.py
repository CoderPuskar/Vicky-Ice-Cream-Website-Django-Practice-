from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


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
    message = ""
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        if name and email and phone and description:
            contact = Contact(name=name, email=email, phone=phone, description=description, date=datetime.today())
            contact.save()
            messages.success(request, "Profile details updated.")
            message = "Your message has been sent!"
        else:
            message = "Please fill all fields."

    return render(request, 'contact.html', {'message': message})


        


    return render(request,'contact.html')


    