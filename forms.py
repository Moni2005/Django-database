from django import forms 
from .models import LandingPageEntry

class LandingPageEntryModelForm(forms.ModelForm):
    name = forms.CharField(required = False)
    email = forms.EmailField()
    email2 = forms.EmailField(label="confirm email")
    
    
    class Meta:
        model = LandingPageEntry
        fields = ['name', 'email']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:

            default_css_class = 'form-control'
            new_attrs = {
                "class" : default_css_class,
                "id" : f"{field}",
                "placeholder" : f"Your{field}",
            }
            if field == "email2":
                new_attrs["placeholder"] = f"Confirm your email"
                
            self.fields[field].widget.attrs.update(new_attrs)
    
    def clean(self):
        data = self.cleaned_data
        email = data.get('email')
        email2 = data.get("email2")
        if email2 != email:
            self.add_error('email', "Your email isn't matching!")
        return data
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email.endswith("gmail.com"):
            self.add_error('email', "You cannot use gmail!")
        return email

class LandingPageForm(forms.Form):
    name = forms.CharField(required = False)
    email = forms.EmailField()
    email2 = forms.EmailField(label="confirm email")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:

            default_css_class = 'form-control'
            new_attrs = {
                "class" : default_css_class,
                "id" : f"{field}",
                "placeholder" : f"Your{field}",
            }
            if field == "email2":
                new_attrs["placeholder"] = f"Confirm your email"
                
            self.fields[field].widget.attrs.update(new_attrs)
    
    def clean(self):
        data = self.cleaned_data
        email = data.get('email')
        email2 = data.get("email2")
        if email2 != email:
            self.add_error('email', "Your email isn't matching!")
        return data
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email.endswith("gmail.com"):
            self.add_error('email', "You cannot use gmail!")
        return email