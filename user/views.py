from django.shortcuts import render, redirect
from .models import * 
from .forms import * 
from .backends import CustomPhoneNumberBackend
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required  
from .utils import * 
from django.contrib import messages



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
            messages.add_message(request, messages.SUCCESS, "تم إنشاء حسابك بنجاح، قم بالتحقق من رقم الهاتف للتمتع بمزايا إضافة الإعلانات")
            return redirect('page:index') 


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
            messages.add_message(request, messages.SUCCESS, "تم إنشاء حسابك بنجاح، قم بالتحقق من رقم الهاتف للتمتع بمزايا إضافة الإعلانات")
            return redirect('page:index') 
        

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
            messages.add_message(request, messages.SUCCESS, "تم إنشاء حسابك بنجاح، قم بالتحقق من رقم الهاتف للتمتع بمزايا إضافة الإعلانات")
            return redirect('page:index') 

            

    context = {
        'form': form 
    }

    return render(request, 'user/signup.html', context)

def user_login(request):

    if request.POST: 
        phone_number_input = request.POST.get('phone_number_input') 
        password= request.POST.get('password_input') 
        
        try:
            user = CustomPhoneNumberBackend().authenticate(request, phone_number=phone_number_input, password=password)
        except:
            # Catch any exceptions during authentication and display an error message
            messages.add_message(request, messages.ERROR, "رقم الهوية أو كلمة المرور غير صحيحة. أعد المحاولة مرة أخرى")
            return redirect('user:user-login')

        if user is not None:
            # If authentication is successful, log in the user
            login(request, user=user, backend='user.backends.CustomIdBackend')
            messages.add_message(request, messages.SUCCESS, "تم تسجيل الدخول بنجاح")
            return redirect('page:index')
        else:
            # If authentication fails, display an error message
            messages.add_message(request, messages.ERROR, "رقم الهوية أو كلمة المرور غير صحيحة. أعد المحاولة مرة أخرى")
            return redirect('user:user-login')

    

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
        if request.POST: 
            otp = generate_otp() 
            request.session['otp'] = otp 
            send_otp('192', otp)
            print('message sent') 
            return redirect('user:check-otp')
    else: 
        ## already verified 
        return render(request, 'user/already-verified.html')
    context = {} 
    return render(request, 'user/verify-phone-number.html', context)

@login_required
def check_otp(request): 
    user =  request.user

    if user.phone_number_verify_status == False: 
        if request.POST: 
            stored_otp = request.session['otp']
            otp_input = request.POST.get('otp-input')  
            print(type(stored_otp))
            print(type(otp_input))
            print(otp_input) 
            if otp_input != None: 
                print('otp input is not none') 
                if str(stored_otp) == otp_input: 
                    print('yes') 
                    user_obj = CustomUser.objects.get(phone_number=user.phone_number)
                    user_obj.phone_number_verify_status = True 
                    user_obj.save() 
                    
                    return redirect('user:user-verified')


                else: 
                    return redirect('user:check-otp') 
            
    else: 
        return redirect('user:verify-phone-number') 

    context = {} 
    return render(request, 'user/check-otp.html', context)

def user_verified(request): 
    context = {} 
    return render(request, 'user/user-verified.html', context)


@login_required
def profile(request):
    user= request.user
    role = user.role 
    
    if role =='user':
        form =UserUpdateForm(instance=user)
    elif role == 'real_estate_office':
        form = OfficeUpdate(instance=user)
    elif role == 'real_estate_marketer': 
        form = MarkterUpdate(instance=user)
    else: 
        form =UserUpdateForm(instance=user)

    if request.POST:
        if role=='user': 
            form = UserUpdateForm(request.POST, instance=user) 
        elif role=='real_estate_office': 
            form = OfficeUpdate(request.POST, instance=user) 
        elif role=='real_estate_marketer':
            form = MarkterUpdate(request.POST, instance=user) 

        if form.is_valid():
            form.save() 
            return redirect('user:profile') 
        

    context = {
        'form': form, 
    } 
    return render(request, 'user/profile.html', context)