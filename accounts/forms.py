from django import forms
from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,


)
User = get_user_model()

class UserLogInForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    #THIS METHOD IS ALWAYS CALLED WHEN CLEANED_DATA IS CALLED IN VIEWS.PY
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            # user = authenticate(username=username, password=password)
            # if not user:
            #     raise forms.ValidationError("This user does not exist")
            #
            # if not user.check_password(password):
            #     raise forms.ValidationError("Incorrect Password")
            #
            # if not user.is_active:
            #     raise forms.ValidationError("User No Longer active")
            user_qs = User.objects.filter(username=username)
            if user_qs.count() == 0:
                raise forms.ValidationError("The user does not exist")
            else:
                user = authenticate(username=username, password=password)
                if not user:
                    raise forms.ValidationError("Incorrect password")
                if not user.is_active:
                    raise forms.ValidationError("This user is no longer active")

        return super(UserLogInForm,self).clean(*args,**kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email Address')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'

        ]

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails Don't Match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This Email has already been registered")
        return email

























