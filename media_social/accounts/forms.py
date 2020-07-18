from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        fields= ('username','email','password1','password2')
        model = get_user_model()

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['username'].label = 'Your UserName'
            self.fields['email'].label = 'Your Email'
            self.fields['password1'].label = 'Your Password'
            self.fields['password2'].label = 'Password Again'
