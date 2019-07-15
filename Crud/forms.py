from django import forms
from Crud.models import King,Dummy


class king(forms.ModelForm):



    class Meta:
        model = King
        fields = '__all__'

class dummy(forms.ModelForm):

    class Meta:
        model = Dummy
        fields = '__all__'
