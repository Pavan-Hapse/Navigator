from django.shortcuts import render

# Create your views here.


def function(request):
    return render(request, 'index.html' ,{'link':'Pavan Website','see': ' http://127.0.0.1:8000/'})

def expression(request):
    a=int(request.POST['Text1'])
    b=int(request.POST['Text2'])
    c=a+b
    return render(request,'output.html',{'Result' : c}) 