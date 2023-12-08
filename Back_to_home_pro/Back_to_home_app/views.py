from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.shortcuts import render , redirect , HttpResponseRedirect
from .models import *
from datetime import *
# Create your views here.
def index(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        if  code.strip():
            search = userclass.objects.filter(code=code).first()
            if search :
                return  HttpResponseRedirect(f'/data/?id={code}')
            else:
                check = "False";
                return render(request,'index.html' , {'check':check})
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
            check = "False";
            return render(request,'add_data.html' , {'check':check})
        else:
            data = userclass(image = image_user ,
                                        name = name_user ,
                                        address = address_user ,
                                        phonenumber= phone1 ,
                                        phonenumber2 = phone2 ,
                                        code = code_user
                            )
            data.save()
            return HttpResponseRedirect(f'/add_successfuly/?code={code_user}')
    return render(request,'add_data.html')
@login_required(login_url='index')
def invalid_id(request):
    return render(request,'invalid_id.html')
def add_succ(request):
    code = request.GET.get('code')
    return render(request,'add_succ.html',{'code': code})
@login_required(login_url='index')
def invalid_ids(request):
    return render(request,'invalid_ids.html')
def data(request):
    id = request.GET.get('id')
    user = userclass.objects.filter(code=id).first()
    if user:
      return render(request,'data_page.html' , {'kide' : user})
    else:
      return  redirect (invalid_ids)
@login_required(login_url='admin_page')
def admin_home(request):
    loop = userclass.objects.all()
    id_of_user = request.POST.get('id')
    check = "false"
    try:
        user_instance = userclass.objects.get(code=id_of_user)
        if user_instance is not None:
             user_instance.delete()
             check = "true"
        else:
             check = "false"
             return render(request, 'admin_home.html', {'table_users': loop, 'check': check})
    except userclass.DoesNotExist:
        check = "false"
    return render(request, 'admin_home.html', {'table_users': loop, 'check': check})

def admin_page(request):
    if request.method == 'POST':
       user_name = request.POST.get('user_name')
       password = request.POST.get('pass')
       admin = admin_table.objects.filter(user_name=user_name, password=password).first()
       if admin:
           return redirect(admin_home)
       else:
           check = "false"
           return render(request , 'admin_page.html' , {'check':check})
    return render(request , 'admin_page.html')