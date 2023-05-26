from django.contrib.auth.forms import UserCreationForm, UserChangeForm # new

from .models import CustomUser # new

class CustomUserCreationForm(UserCreationForm):
  class Meta(UserCreationForm):
    model = CustomUser
    fields = UserCreationForm.Meta.fields + ('email', 'username',) # new
    
class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = CustomUser
    fields = UserChangeForm.Meta.fields