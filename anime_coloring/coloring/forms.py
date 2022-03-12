from django import forms

class color_form(forms.Form):

    image = forms.ImageField(label="Upload your image here")
    #r = forms.IntegerField(label = "r", max_value=255, min_value=0)
    #g = forms.IntegerField(label = "g", max_value=255, min_value=0)
    #b = forms.IntegerField(label = "b", max_value=255, min_value=0)