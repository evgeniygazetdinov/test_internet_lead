
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from auths.forms import UserCreationForm as UserForm
from auths.models import CustomUser

def index(request):
    return render(request, 'auths/auths.html',)

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            first_name = user_form.cleaned_data.get('first_name')
            last_name = user_form.cleaned_data.get('last_name')
            email = user_form.cleaned_data.get('email')
            password = user_form.cleaned_data.get('password1')
            new_user = CustomUser.objects.create(first_name=first_name, last_name = last_name, username = first_name+ last_name,email=email, password=password)
            new_user = user_form.save(commit=False)
            new_user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'auths/auths.html',{'user_form':user_form})






@login_required
def home(request):
  return render(request, 'auths/home.html')