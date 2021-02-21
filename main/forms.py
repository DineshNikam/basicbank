from django import forms
from .models import customer, transfer


customers=customer.objects.all()
cust=[]
for c in customers:
    cust.append((c.id,c.name))
class createForm(forms.Form):

    # name = forms.CharField(label="Name",max_length=200)
    fromc = forms.CharField(
        label='Transfer from ', widget=forms.Select(choices=cust),)
    name = forms.CharField(
        label='Transfer to  ', widget=forms.Select(choices=cust),)
    
    amount= forms.IntegerField()
