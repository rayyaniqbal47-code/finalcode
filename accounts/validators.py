import os
from django.core.exceptions import ValidationError


def validate_resume_extension(value):

    ext = os.path.splitext(value.name)[1].lower()

    valid_extensions = ['.pdf', '.docx']

    if ext not in valid_extensions:
        raise ValidationError('Only PDF and DOCX files are allowed.')
    

    