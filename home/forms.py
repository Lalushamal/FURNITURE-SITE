from django import forms
from .models import Furniture,Address, Order,Reviews

class MakePost(forms.ModelForm):
    class Meta:
        model = Furniture
        fields = '__all__'
class AddPost(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
class ReviewPost(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = '__all__'