from django.shortcuts import redirect, render

from .models import Contact

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        
        number = request.POST['number']
        email = request.POST['email']
        massage=request.POST['massage']
        
        new_contact = Contact(name=name,  number=number, email=email,massage=massage)
        new_contact.save()

        print(new_contact)
        
        return redirect('index')
    
    return render(request, 'index.html')

def about(request):
    
    return render(request, 'about.html')


def contact(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        
        number = request.POST['number']
        email = request.POST['email']
        massage=request.POST['massage']
        
        new_contact = Contact(name=name,  number=number, email=email,massage=massage)
        new_contact.save()

        print(new_contact)
        
        return redirect('index')
    return render(request, 'contact.html')

def medicine(request):
    
    return render(request, 'medicine.html')

def news(request):
    
    return render(request, 'news.html')
