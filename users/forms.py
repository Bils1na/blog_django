from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    email = forms.EmailField(label="Email", widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ("username", "email")

    def _confirm_email(self):
        if User.objects.filter(email=self.cleaned_data.get('email')).exists():
            raise forms.ValidationError("Email already exists")
        
    def _confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        print(self.cleaned_data)
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
    
    def clean(self):
        self._confirm_password()
        self._confirm_email()
    
    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
