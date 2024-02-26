from django.shortcuts import render


# Create your views here.
def index(request):
     return render(request, 'index.html')


def innerpage(request):
    render(request, 'inner-page.html')
