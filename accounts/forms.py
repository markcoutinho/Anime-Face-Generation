from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField()        
    error_messages = {
        'password_mismatch': "Passwords do not match!",
        'email_exist':'Email Exists!',
        'user_exist':'Username Exists!'
    }
    class Meta :
        model = User
        fields = ['username','email','password1','password2']

    def clean(self):             
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')        
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:            
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch'
            ) 
      
        if User.objects.filter(email=email).exists() :              
            raise forms.ValidationError(
                self.error_messages['email_exist'],
                code='email_exist'
            )        
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                self.error_messages['user_exist'],
                code='user_exist'
            )            

        return self.cleaned_data

        
