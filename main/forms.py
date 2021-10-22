from django.forms import ModelForm
from main.models import Users

class UserForm(ModelForm):
    
    class Meta:
        model = Users
        fields = ("username","email")
