from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'John',
            'id': 'inputUsername'
        })
    )

    email = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'example@user.com',
            'id': 'inputEmailAddress'
        })
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control border-end-0',
            'placeholder': 'Enter Password',
            'id': 'inputChoosePassword'
        })
    )

    password_confirm = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control border-end-0',
            'placeholder': 'Confirm Password',
            'id': 'inputConfirmPassword'
        })
    )

    agree_terms = forms.BooleanField(
        required=True,
        label='I read and agree to Terms & Conditions',
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
            'id': 'flexSwitchCheckChecked',
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match.")
