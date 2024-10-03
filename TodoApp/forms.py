from typing import Any
from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from .models import Task
from django.contrib.auth.forms import UserCreationForm ,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User 

class TaskForm(forms.ModelForm):
    class Meta:
        model =Task
        fields = ['title','description','priority','category']
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['description'].widget.attrs.update({'class':'form-control'})
        self.fields['priority'].widget.attrs.update({'class':'form-select'})
        self.fields['category'].widget.attrs.update({'class':'form-select'})

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','password1','password2']
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(RegisterForm,self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})

class  PasswordChange(PasswordChangeForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
class PasswordReset(PasswordResetForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
class PasswordResetConfirm(SetPasswordForm):
    def __init__(self,   *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})