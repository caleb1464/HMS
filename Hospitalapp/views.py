from django.shortcuts import render, redirect
from Hospitalapp.models import Members, Message, Users


# Create your views here.
def index(request):
    if request.method == 'POST':
        messages = Message(name=request.POST['name'], email=request.POST['email'], subject=request.POST['subject'],
                           message=request.POST['message'])
        messages.save()
        return redirect('/')
    else:
        return render(request, 'index.html')


def innerpage(request):
    return render(request, 'inner-page.html')


def register(request):
    if request.method == 'POST':
        members = Members(username=request.POST['username'], email=request.POST['email'],
                          password=request.POST['password'])
        members.save()
        return redirect('/register')
    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def upload(request):
    return render(request, 'upload.html')


def details(request):
    details = Message.objects.all()
    return render(request, 'details.html', {'details': details})


def value(request):
    value = Users.objects.all()
    return render(request, 'value.html', {'value': value})
