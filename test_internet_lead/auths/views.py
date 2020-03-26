
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from auths.forms import UserCreationForm as UserForm
from auths.models import CustomUser
from django.shortcuts import redirect
from django.contrib import messages


def index(request):
    return render(request, 'auths/auths.html',)

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data.get('first_name') + user_form.cleaned_data.get('last_name')
            if CustomUser.objects.filter(username=username ).exists():
                messages.info(request,"пользователь {} уже существует".format(username))
            else:
                first_name = user_form.cleaned_data.get('first_name')
                last_name = user_form.cleaned_data.get('last_name')
                email = user_form.cleaned_data.get('email')
                password = user_form.cleaned_data.get('password1')
                new_user = CustomUser.objects.create(first_name=first_name, last_name = last_name, username = username, email=email, password=password)
                registered = True
                messages.info(request,"пользователь {} cоздан".format(first_name+last_name))
                redirect('/home')
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'auths/auths.html',{'user_form':user_form})






@login_required
def home(request):
  return render(request, 'auths/home.html')




#TODO FIX mechanics in redirect
#FIX front end
#and add union colors