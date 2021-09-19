from django import forms

class InterestForm(forms.Form):
        amount=forms.FloatField(label='Amount')
        rate=forms.FloatField(label="Interest rate" ,min_value=5 ,max_value=50)

