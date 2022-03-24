from urllib.request import Request
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
import re 
# Create your views here.
def signin(request):
    if request.method == 'POST' and 'btnsignin' in request.POST:
        username = request.POST['user']
        password = request.POST['pass']
        user = auth.authenticate(username = username , password=password)
        if user is not None:
            if 'rememberme' not in request.POST:
                request.session.set_expiry(0)
            auth.login(request , user)
        else:
            messages.error(request , 'User name or Password invaild')
        return redirect('signin')
        
    else:
        return render (request , 'accounts/signin.html')

def signup(request):
    if request.method == 'POST' and 'sumbit' in request.POST:
        firstname = None
        lastname  = None
        username  = None
        email     = None
        password  = None
        policy = None
        is_add = None
        if 'user' in request.POST : username = request.POST['user']
        else : messages.error(request , 'error in username')

        if 'fname' in request.POST : firstname = request.POST['fname']
        else : messages.error(request , 'error in firstname')

        if 'lname' in request.POST : lastname = request.POST['lname']
        else : messages.error(request , 'error in lastname')

        if 'email' in request.POST : email = request.POST['email']
        else : messages.error(request , 'error email')

        if 'pass' in request.POST : password = request.POST['pass']
        else: messages.error(request , 'error password')

        if 'policy' in request.POST : policy = request.POST['policy']

        #check value 

        if firstname and lastname and username and email and password:
            if policy == 'on':
                #check the user name 
                if User.objects.filter(username=username).exists():
                    messages.error(request , 'The user name is taken')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request , 'The Email is taken')
                    else:
                        patt = "^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
                        if re.match(patt,email):
                            user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email,
                            username=username , password=password)
                            user.save()
                            firstname = ''
                            lastname  = ''
                            username = ''
                            email = ''
                            password = ''
                            policy = None   
                            messages.success(request, 'Your Account is Created')
                            is_add = True
                        else:
                            messages.error(request , 'The Email is Not Vaild')

            else:
                messages.error(request , 'Please Agree Policy')
        else:
            messages.error(request , 'Check Empty Fields')

        return render (request , 'accounts/signup.html',{
            'fname':firstname,
            'lname':lastname,
            'email':email,
            'is_add':is_add
        })
            

    else:
        return render (request , 'accounts/signup.html')


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('index')