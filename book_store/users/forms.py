from typing import Any
from django import forms
from utils.field_validation import is_number, check_password

class SignupForm(forms.Form):
    name = forms.CharField(max_length=50)
    number = forms.CharField(max_length=12)
    password = forms.CharField(max_length=50)
    code = forms.IntegerField()

    def clean(self) -> dict[str, Any]:
        cd = self.cleaned_data
        if check_password(cd.get("password")):
            raise ValueError("password is less than 8")
        if is_number(cd.get("number")):
            raise ValueError("invalid number")
        print("clean i'm here")
        return super().clean()
    

class LoginForm(forms.Form):
    number = forms.CharField(max_length=12)
    password = forms.CharField(max_length=50)
    code = forms.IntegerField()

    def clean(self) -> dict[str, Any]:
        cd = self.cleaned_data
        if is_number(cd.get("number")):
            raise ValueError("invalid number")
        return super().clean()