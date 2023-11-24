from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.shortcuts import render , redirect , HttpResponseRedirect
from .models import *
# Create your views here.
def index(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        if  code.strip():
            search = userclass.objects.filter(code=code).first()
            if search :
                return  HttpResponseRedirect(f'/data/?id={code}')
            else:
                return redirect(invalid_ids)
        else: 
            return render(request , 'index.html')
    return render(request,'index.html')
def add_data(request):
    if request.method == 'POST':
        image_user = request.FILES.get('image')
        name_user = request.POST.get('name')
        address_user = request.POST.get('address')
        phone1 = request.POST.get('phone_number1')
        phone2 = request.POST.get('phone_number2')
        code_user = request.POST.get('code')
        search = userclass.objects.filter(code=code_user).first()
        if search:
            return redirect(invalid_id)
        else:
            data = userclass(image = image_user ,
                                        name = name_user ,
                                        address = address_user ,
                                        phonenumber= phone1 ,
                                        phonenumber2 = phone2 , 
                                        code = code_user
                            )
            data.save()
            return redirect(add_succ)
    return render(request,'add_data.html')
@login_required(login_url='index')
def invalid_id(request):
    return render(request,'invalid_id.html')
@login_required(login_url='index')
def add_succ(request):
    return render(request,'add_succ.html')
@login_required(login_url='index')
def invalid_ids(request):
    return render(request,'invalid_ids.html')
@login_required(login_url='index')
def data(request):
    id = request.GET.get('id')
    user = userclass.objects.filter(code=id).first()
    return render(request,'data_page.html' , {'kide' : user})