from django import forms 
from django.contrib.auth.models import User

################ Registration Form#################

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("email",)

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        
        if password and password2 and password != password2:
            raise forms.ValidationError("Password didn't match")
        return password2
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user already exists")
        return email
    
    def save(self, commit=True):
        user = super().save(commit="False")
        user.set_password(self.cleaned_data["password"])
        user.email = self.cleaned_data.get("email")

        if commit:
            user.save()

        user.username = f"user{user.id}"

        if commit:
            user.save()

        return user
    
################ Registration Form#################

################ Login Form#################

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email"
    )

    password = forms.CharField(
        label="Password",
        widget = forms.PasswordInput
    )
