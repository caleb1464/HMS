from django.shortcuts import render, redirect
from Hospitalapp.models import Members, Message, Users, ImageModel
from Hospitalapp.forms import ImageUploadForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        messages = Message(name=request.POST['name'], email=request.POST['email'], subject=request.POST['subject'],
                           message=request.POST['message'])
        messages.save()
        return redirect('/')
    else:
        return render(request, 'index.html')


def inner(request):
    return render(request, 'inner-page.html')


def register(request):
    if request.method == 'POST':
        members = Members(username=request.POST['username'], email=request.POST['email'],
                          password=request.POST['password'])
        members.save()
        return redirect('/login')
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


def adminhome(request):
    if request.method == 'POST':
        if Members.objects.filter(username=request.POST['username'],
                                  password=request.POST['password']).exists():
            member = Members.objects.get(username=request.POST['username'],
                                         password=request.POST['password'])
            return render(request, 'adminhome.html', {'member': member})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})


def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'showimages.html', {'images': images})


def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')
