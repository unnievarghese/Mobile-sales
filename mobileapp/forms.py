from django.forms import ModelForm
from django import forms
from mobileapp.models import mobile_model,buyer_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class userregistrationform(UserCreationForm):
    class Meta():
        model=User         #builtin model
        fields=['username','first_name','last_name','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'}),
        }

class mobile_form(ModelForm):
    class Meta:
        model=mobile_model
        fields='__all__'
    def clean(self):
        cleaned_data=super().clean()
        price=cleaned_data.get('price')
        if price<500:
            msg='Enter a valid price!'
            self.add_error('price',msg)

class edit_mobile_form(ModelForm):
    class Meta:
        model=mobile_model
        fields='__all__'

class edit_order_form(ModelForm):
    stat=(('New order','New order'),('Order proccessed','Order proccessed'),('Pending','Pending'),('Dispached','Dispached'))
    status = forms.ChoiceField(choices=stat, initial='New order')

    class Meta:
        model=buyer_model
        fields='__all__'
        widgets = {
            'product': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'buyer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'buyer_address': forms.Textarea(attrs={'class': 'form-control'}),
            'buyer_mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

class buyer_form(ModelForm):
    status=forms.CharField(initial='New order',disabled=True)

    class Meta:
        model=buyer_model
        fields=['buyer_name','buyer_address','buyer_mobile','user','product']
        widgets={
            'product':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
            'buyer_name':forms.TextInput(attrs={'class':'form-control'}),
            'buyer_address': forms.Textarea(attrs={'class': 'form-control'}),
            'buyer_mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'user':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
        }

