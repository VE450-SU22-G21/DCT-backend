from django import forms

class keyForm(forms.Form):
    key = forms.CharField(label='key', max_length=256)
    # created_at = forms.DateTimeField(label='time_stamp',auto_now_add=True)
