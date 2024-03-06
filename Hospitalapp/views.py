import json

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from requests.auth import HTTPBasicAuth

from Hospitalapp.credentials import MpesaAccessToken, LipanaMpesaPpassword
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


def token(request):
    consumer_key = 'gUqBhTha6izBkV1Gm8hNoorzH6GmYb7sRaXaRsTBMKahVLFX'
    consumer_secret = '6M4WbXYMGPeJAv2GNrdYR2pNzf4lcAjUc7DVXzblQY1Yj08D99zUPGrWtEMeYAtf'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token": validated_mpesa_access_token})


def pay(request):
    return render(request, 'pay.html')


def stk(request):
    if request.method == "POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Apen Softwares",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse(response)
