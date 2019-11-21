from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authapp.forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_page_view(request):
    return render(request, 'authapp/home.html')

@login_required
def java_exam_view(request):
    return render(request, 'authapp/javaexams.html')

@login_required
def python_exam_view(request):
    return render(request, 'authapp/Pythonexam.html')

@login_required
def oracle_exam_view(request):
        return render(request, 'authapp/oracleexam.html')


def log_out_view(request):
    return render(request, 'authapp/logout.html')

def sign_up_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form = SignUpForm(request.POST)
        user= form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'authapp/signup.html', {'form':form})
