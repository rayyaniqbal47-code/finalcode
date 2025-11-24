from django import forms
from .models import Job

class AddJobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['title', 'company_name', 'description', 'state', 'city', 'job_type', 'experience_level', 
                  'total_years_of_experience_required', 'salary_min', 'salary_max', 'skills']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input w-full p-2 border rounded-lg',
                'id': 'job-title',
                'placeholder': 'Enter job title'
            }),
            'company_name': forms.TextInput(attrs={
                'class': 'form-input w-full p-2 border rounded-lg',
                'id': 'company-name',
                'placeholder': 'Enter company name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-textarea w-full p-2 border rounded-lg',
                'id': 'job-description',
                'placeholder': 'Describe the job responsibilities'
            }),
            'state': forms.Select(attrs={
                'class': 'form-select w-full p-2 border rounded-lg',
                'id': 'job-state',
                'placeholder': 'Select state'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-select w-full p-2 border rounded-lg',
                'id': 'job-city',
                'placeholder': 'Select city'
            }),
            'job_type': forms.Select(attrs={
                'class': 'form-select w-full p-2 border rounded-lg',
                'id': 'job-type',
                'placeholder': 'Select job type'
            }),
            'experience_level': forms.Select(attrs={
                'class': 'form-select w-full p-2 border rounded-lg',
                'id': 'experience-level',
                'placeholder': 'Select experience level'
            }),
            'total_years_of_experience_required': forms.NumberInput(attrs={
                'class': 'form-input w-full p-2 border rounded-lg',
                'id': 'experience-required',
                'placeholder': 'Enter required years of experience'
            }),
            'salary_min': forms.NumberInput(attrs={
                'class': 'form-input w-full p-2 border rounded-lg',
                'id': 'salary-min',
                'placeholder': 'Enter minimum salary'
            }),
            'salary_max': forms.NumberInput(attrs={
                'class': 'form-input w-full p-2 border rounded-lg',
                'id': 'salary-max',
                'placeholder': 'Enter maximum salary'
            }),
            'skills': forms.SelectMultiple(attrs={
                'class': 'form-select w-full p-2 border rounded-lg',
                'id': 'skills',
                'placeholder': 'Select required skills'
            })
        }


        
