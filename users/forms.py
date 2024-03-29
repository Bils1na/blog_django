from django import forms
from users.models import BlogUser


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    email = forms.EmailField(label="Email", widget=forms.EmailInput)

    class Meta:
        model = BlogUser
        fields = ("username", "email")

    def _confirm_email(self):
        confirm_email = self.cleaned_data.get("email").lower()
        if BlogUser.objects.filter(email=confirm_email).exists():
            raise forms.ValidationError("Email already exists.")
        return confirm_email
    
    def _confirm_username(self):
        confirm_username = self.cleaned_data.get("username").lower()
        if BlogUser.objects.filter(username=confirm_username).exists():
            raise forms.ValidationError("Username already exists.")
        return confirm_username
        
    def _confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return confirm_password
    
    def clean(self):
        self._confirm_password()
        self._confirm_username()
        self._confirm_email()
    
    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = BlogUser
        fields = ["email", "first_name", "last_name", "date_of_birth"]

    def _confirm_email(self):
        confirm_email = self.cleaned_data.get("email").lower()
        current_user = self.instance
        current_email = current_user.email.lower()
        if confirm_email != current_email:
            if BlogUser.objects.filter(email=confirm_email).exists():
                raise forms.ValidationError("Email already exists.")
        return confirm_email

    def clean(self):
        self._confirm_email()

