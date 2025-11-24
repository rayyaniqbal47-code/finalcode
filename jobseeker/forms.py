from django import forms 
from accounts.models import CustomUserProfile , CustomUser
from jobseeker.models import Experience , Education


class JobSeekerCustomUserForm(forms.ModelForm):
        class Meta:
            model = CustomUser
            fields = ['first_name' , 'last_name']

            widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors duration-300',
                'placeholder': 'Enter your first name',
                'id': 'first_name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors duration-300',
                'placeholder': 'Enter your last name',
                'id': 'last_name'
            }),
        }



class JobSeekerProfileForm(forms.ModelForm):

    class Meta:
        model = CustomUserProfile
        fields = ['bio' , 'resume']
        
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors duration-300 resize-none',
                'placeholder': 'Write a short bio',
                'rows': 4,
                'id': 'bio'
            }),
            'resume': forms.FileInput(attrs={
                'class': 'w-full text-gray-700 border border-gray-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-colors duration-300',
                'id': 'resume'
            }),
        }


class ExperienceForm(forms.ModelForm):
     
    class Meta:
        model = Experience
        fields = ['company_name' , 'role' , 'years']

        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors duration-300',
                'id': 'company_name',
                'placeholder': 'e.g. TechSolutions Inc.',
            }),
            'role': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors duration-300',
                'id': 'role',
                'placeholder': 'e.g. Senior Frontend Developer',
            }),
            'years': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors duration-300',
                'id': 'years',
                'placeholder': 'e.g. 2 years 6 months',
            }),
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution_name', 'degree', 'start_year', 'end_year']

        widgets = {
            'institution_name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors duration-300',
                'placeholder': 'e.g. Stanford University',
                'id': 'institution_name',
            }),
            'degree': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors duration-300',
                'placeholder': 'e.g. Bachelor of Science in Computer Science',
                'id': 'degree',
            }),
            'start_year': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors duration-300',
                'placeholder': 'e.g. 2018',
                'min': 1900,
                'max': 2030,
                'id': 'start_year',
            }),
            'end_year': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors duration-300',
                'placeholder': 'e.g. 2022',
                'min': 1900,
                'max': 2030,
                'id': 'end_year',
            }),
        }



