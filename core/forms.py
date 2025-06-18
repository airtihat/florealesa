from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='البريد الإلكتروني')
    phone = forms.CharField(label='رقم الجوال', max_length=15, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")  # phone غير موجود في model User

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("هذا البريد الإلكتروني مستخدم بالفعل.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if not phone.startswith("05") or not phone.isdigit():
            raise forms.ValidationError("رقم الجوال غير صالح. يجب أن يبدأ بـ 05 ويتكوّن من أرقام فقط.")
        return phone

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        # يمكنك هنا حفظ رقم الجوال في نموذج مخصص أو جدول آخر إذا لزم
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='اسم المستخدم',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='كلمة المرور',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
