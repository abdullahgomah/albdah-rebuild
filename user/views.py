from django.shortcuts import render, redirect
from .models import * 
from .forms import * 
from .backends import CustomIdBackend
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required  
from .utils import generate_otp 
from django.contrib import messages

from dotenv import load_dotenv 
from twilio.rest import Client
from twilio.base.exceptions import TwilioException
import os 

load_dotenv() 

ACCOUNT_SID = os.getenv("ACCOUNT_SID") 
AUTH_TOKEN = os.getenv("AUTH_TOKEN") 

client = Client("ACb93085c0516e9504af4446acddce07ed", "3cb77c1f1f1d6cae22df4b5dc03ea357")

def send_otp(to, otp): 
    try: 
        message = client.messages.create(
                        body=f"مرحباً بكم في مكتب البداح للعقارات. رمز ال دخول هو {otp}", 
                        from_='+18052197512',
                        to=to 
                    )
    except TwilioException as ex: 
        print(f"Exception is: {ex}") 

# Create your views here.
def before_register(request): 
    context = {} 
    return render(request, 'user/before-login.html', context)


def user_register(request): 
    form = UserForm()

    if request.POST: 
        form = UserForm(request.POST) 
        if form.is_valid(): 
            form.save(commit=False) 
            form.instance.role = 'user' 
            form.save() 
            return redirect('user:user-login') 


    context = {
        'form': form 
    }
    return render(request, 'user/signup.html', context)


def office_register(request): 
    form = OfficeRegister() 

    if request.POST: 
        form = OfficeRegister(request.POST) 
        if form.is_valid(): 
            form.save(commit=False) 
            form.instance.role = 'real_estate_office'
            form.save() 
            return redirect('user:user-login') 
        
        

    context ={ 
        'form': form 
    }

    return render(request, 'user/signup.html', context)
    

def markter_register(request): 
    form = MarkterRegister() 

    if request.POST: 
        form = MarkterRegister(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save(commit=False) 
            form.instance.role = 'real_estate_marketer' 
            form.save() 
            return redirect('user:user-login') 

            

    context = {
        'form': form 
    }

    return render(request, 'user/signup.html', context)

def user_login(request):

    if request.POST: 
        id_number = request.POST.get('id_number_input') 
        password= request.POST.get('password_input') 
        
        try:
            user = CustomIdBackend().authenticate(request, id_number=id_number, password=password)
        except:
            # Catch any exceptions during authentication and display an error message
            messages.add_message(request, messages.ERROR, "رقم الهوية أو كلمة المرور غير صحيحة. أعد المحاولة مرة أخرى")
            return redirect('user:user-login')

        if user is not None:
            # If authentication is successful, log in the user
            login(request, user=user, backend='user.backends.CustomIdBackend')
            return redirect('page:index')
        else:
            # If authentication fails, display an error message
            messages.add_message(request, messages.ERROR, "رقم الهوية أو كلمة المرور غير صحيحة. أعد المحاولة مرة أخرى")
    

    context = {
    } 
    return render(request, 'user/user-login.html', context)


def custom_logout(request): 
    logout(request) 

    return redirect('page:index') 


@login_required
def verify_phone_number(request): 
    user = request.user 
    if user.phone_number_verify_status == False: 
        otp = generate_otp() 
        request.session['otp'] = otp
        number = str(user.phone_number) 
        send_otp(number, otp) 
    else: 
        ## already verified 
        return render(request, 'user/already-verified.html')
    context = {} 
    return render(request, 'user/verify-phone-number.html', context)

@login_required
def check_otp(request): 
    user =  request.user  
    print(user.phone_number)

    if user.phone_number_verify_status == False: 
        stored_otp = request.session['otp']
        if request.POST: 
            otp_input = request.POST['otp-input'] 
            if int(otp_input) == stored_otp: 
                print('yes') 
                user_obj = CustomUser.objects.get(phone_number=user.phone_number)
                user_obj.phone_number_verify_status = True 
                user_obj.save() 
                
                return redirect('user:user-verified')


                print(user_obj) 
            else: 
                return redirect('user:check-otp') 
            
    else: 
        return redirect('user:verify-phone-number') 

    context = {} 
    return render(request, 'user/check-otp.html', context)

def user_verified(request): 
    context = {} 
    return render(request, 'user/user-verified.html', context)