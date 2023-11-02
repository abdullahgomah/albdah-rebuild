from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login 
from .backends import PhoneNumberBackend
from django.core.exceptions import ObjectDoesNotExist 
from .models import Profile, User 
from codes.models import Otp 
from .forms import UserUpdateForm, UpdateProfileForm, SignupForm
from .utils import send_sms

# Create your views here.

@login_required
def profile(request):
    user=  request.user 
    try:
        profile = Profile.objects.get(user=user) 
    except ObjectDoesNotExist: 
        Profile.objects.create(user=user) 
    
    user_update = UserUpdateForm(instance=user)
    profile_update = UpdateProfileForm(instance=profile)
    if request.POST: # Save
        user_update = UserUpdateForm(request.POST, instance=request.user)
        profile_update = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if user_update.is_valid() and profile_update.is_valid():
            # user_update.save(commit=False)
            user_update.save()

            profile_update.save(commit=False) 
            profile_update.user = request.user 
            profile_update.save()
            print('Saved !!!')
            print('save successfully !') # test code 
    else: # Show
        user_update = UserUpdateForm(instance=user)
        profile_update = UpdateProfileForm(instance=profile)

    context = {
        'user_update': user_update,
        'profile_update': profile_update, 
    }
    return render(request, 'accounts/profile.html', context)



def custom_login(request): 
    if request.method == 'POST': 
        phone_number = request.POST.get("phone_number")
        password = request.POST.get('password')

        user = PhoneNumberBackend().authenticate(request, phone_number=phone_number, password=password)
        if user is not None: 
            login(request, user, backend='accounts.backends.PhoneNumberBackend')  
            request.session['pk'] = user.pk 
            send_sms(user.code, user.phone_number)
            return redirect('/accounts/profile')
        else: 
            return render(request, 'accounts/authenticate.html', {'status': 'login', 'error_message': "يوجد خطأ في اسم المستخدم أو كلمة المرور"} )
    



def signup(request): 
    if request.POST: 
        form = SignupForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('custom-login') 

    else: 
        form = SignupForm() 

    context = {
        'form': form 
    }

    return render(request, 'accounts/signup.html', context)


def authenticate_page(request): 
    if request.user.is_authenticated == True: 
        return redirect('/accounts/profile/')
    else: 
        return render(request, 'accounts/authenticate.html', {'status': 'login'} )
    

def send_otp(request): 
    form = SignupForm() 
    if request.POST: 
        phone_number = request.POST.get('phone_number')

        # check if the number is in the database already or not 

        otp = Otp.objects.create(phone_number=phone_number)


        request.session['otp'] = otp.otp 
        request.session['phone_number'] = otp.phone_number 


        send_sms(otp.otp, otp.phone_number) 

        context ={
            'complete_signup': 'true', 
            'status': 'signup', 
            'phone_numebr': request.session.get('phone_number') ,
            'form': form,
        }

        return render(request, 'accounts/authenticate.html', context )
    

def signup(request): 
    # checking otp 
    # prepare error message 
    # signup in case all is fine 

    if request.method == 'POST': 
        otp_input = request.POST.get('otp') 
        otp = request.session.get('otp') 

        if otp_input == otp: 
            ## complete checking 
            form = SignupForm(request.POST) 
            username = form['username'].value() 
            password = form['password'].value() 
            phone_number = request.session.get('phone_number') 

            user = User.objects.create_user(username=username, password=password, phone_number=phone_number)   

            return render(request, 'accounts/authenticate.html', {'status': 'login'}) 
            
        else: 
            ## return again 
            form = SignupForm() 
            context ={
                'complete_signup': 'true', 
                'status': 'signup', 
                'phone_numebr': request.session.get('phone_number') ,
                'form': form,
            }

            return render(request, 'accounts/authenticate.html', context )
           
    context ={
        'complete_signup': 'true', 
        'status': 'signup', 
        'phone_numebr': request.session.get('phone_number') ,
        'form': form,
    }

    return render(request, 'accounts/authenticate.html', context )
    