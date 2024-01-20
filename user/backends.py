from django.contrib.auth.backends import ModelBackend 
from django.contrib.auth import get_user_model 
from django.db.models import Q 

class CustomIdBackend(ModelBackend): 
    def authenticate(self, request, id_number=None, password=None, *args, **kwargs):
        User = get_user_model() 
        try: 
            user = User.objects.get(Q(id_number=id_number))
        except User.DoesNotExist: 
            return None 

        if user.check_password(password): 
            return user 
        return None 