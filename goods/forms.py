from django import forms

from goods.models import Good

class GoodForm(forms.ModelForm):

    class Meta:
        model = Good
        fields = '__all__'

# class ExampleForm(forms.Form):
#    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#    country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
