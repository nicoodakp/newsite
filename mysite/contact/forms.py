from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Subject', 'class':'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Compose','class':'form-control','rows':'10','cols':'40'}))
    from_email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Your Email','class':'form-control'}))
    phone = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'placeholder':'Phone (Optional)','class':'form-control'}))


def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass