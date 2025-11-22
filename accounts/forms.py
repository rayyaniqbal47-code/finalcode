from django import forms 
from accounts.models import CustomUser , CustomUserProfile


class CustomUserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id':"register-password",
        'class':"w-full px-4 py-3 pr-12 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-300",
        'placeholder':"Create a password",
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id':"confirm-password", 
        'class':"w-full px-4 py-3 pr-12 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-300", 
        'placeholder':"Confirm your password",
    }))


    class Meta:
        model = CustomUser
        fields = ['first_name' , 'last_name'  , 'username', 'email', 'password']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-300',
                'placeholder': 'Enter your first name',
                'id': 'first-name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-300',
                'placeholder': 'Enter your last name',
                'id': 'last-name',
            }),
            'username': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-300',
                'placeholder': 'Enter your username',
                'id': 'register-username',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-300',
                'placeholder': 'Enter your email',
                'id': 'register-email',
            }),
        }



    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('password does not match')



