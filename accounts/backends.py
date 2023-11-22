from django.contrib.auth import get_user_model 
from django.contrib.auth.models import User 

class PhoneNumberBackend:
    def authenticate(self, request, phone_number=None, password=None):
        User = get_user_model()

        if phone_number is None or password is None:
            return None

        try:
            user = User.objects.get(phone_number=phone_number)
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None