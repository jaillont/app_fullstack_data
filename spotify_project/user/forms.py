from django.contrib.auth.forms import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class SignupForm(UserCreationForm):
    error_css_class = 'error'
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'input-expand'})
        self.fields['last_name'].widget.attrs.update({'class': 'input-expand'})
        self.fields['email'].widget.attrs.update({'class': 'input-expand'})
        self.fields['spotify_username'].widget.attrs.update({'class': 'input-expand'})
        self.fields['password1'].widget.attrs.update({'class': 'input-expand'})
        self.fields['password2'].widget.attrs.update({'class': 'input-expand'})
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            'email',
            'first_name',
            'last_name', 
            'spotify_username'
        )


class CustomLoginForm(AuthenticationForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update(
      {'class': 'input-expand'}
    )
    self.fields['password'].widget.attrs.update(
      {'class': 'input-expand'}
    )
