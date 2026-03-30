from django import forms
from .models import Faculty, AcademicClass, Student


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Faculty name'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 3, 'placeholder': 'Description (optional)'}),
        }


class AcademicClassForm(forms.ModelForm):
    class Meta:
        model = AcademicClass
        fields = ['name', 'faculty', 'teacher']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Class name'}),
            'faculty': forms.Select(attrs={'class': 'form-select'}),
            'teacher': forms.Select(attrs={'class': 'form-select'}),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'full_name', 'profile_image', 'enrollment_year',
            'faculty', 'academic_class', 'phone', 'guardian_phone',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Full name'}),
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-file', 'accept': 'image/*'}),
            'enrollment_year': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'e.g. 2025'}),
            'faculty': forms.Select(attrs={'class': 'form-select'}),
            'academic_class': forms.Select(attrs={'class': 'form-select'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Phone number'}),
            'guardian_phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Guardian phone'}),
        }


class StudentWebcamForm(forms.Form):
    """Form for capturing student photo via webcam."""
    full_name = forms.CharField(
        max_length=300,
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Full name'})
    )
    enrollment_year = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'e.g. 2025'})
    )
    faculty = forms.ModelChoiceField(
        queryset=Faculty.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    academic_class = forms.ModelChoiceField(
        queryset=AcademicClass.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    phone = forms.CharField(
        max_length=20, required=False,
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Phone number'})
    )
    guardian_phone = forms.CharField(
        max_length=20, required=False,
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Guardian phone'})
    )
    webcam_image = forms.CharField(
        widget=forms.HiddenInput(),
        help_text='Base64-encoded webcam capture'
    )
