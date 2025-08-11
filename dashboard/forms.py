from django import forms 
from .models import Phone

class PhoneForm(forms.ModelForm):

    class Meta:
        model = Phone
        fields = "__all__"
        widgets = {
            "banner" : forms.FileInput(
                attrs = {
                    "class" : "form-control"
                }
            ),
            "model_name" : forms.TextInput(
                attrs = {
                    "class" : "form-control"
                }
            ),
            "brand" : forms.Select(
                attrs = {
                    "class" : "form-control"
                }
            ),
            "instock" : forms.NumberInput(
                attrs = {
                    "class" : "form-control"
                }
            ),
            "price" : forms.NumberInput(
                attrs = {
                    "class" : "form-control"
                }
            ),
            "os" : forms.Textarea(
                attrs = {
                    "class" : "form-control",
                    "rows" : 3,
                    "cols" : 20
                }
            ),
            "cpu" : forms.Textarea(
                attrs = {
                    "class" : "form-control",
                    "rows" : 3,
                    "cols" : 20
                }
            ),
            "ram" : forms.Select(
                attrs = {
                    "class" : "form-control"
                }
            ),
            "storage" : forms.Select(
                attrs = {
                    "class" : "form-control"
                }
            ),
            "battery" : forms.Textarea(
                attrs = {
                    "class" : "form-control",
                    "rows" : 3,
                    "cols" : 20
                }
            ),
            "dimension" : forms.Textarea(
                attrs = {
                    "class" : "form-control",
                    "rows" : 3,
                    "cols" : 20
                }
            ),
            "screen" : forms.Textarea(
                attrs = {
                    "class" : "form-control",
                    "rows" : 3,
                    "cols" : 20
                }
            ),
            "resolution" : forms.Textarea(
                attrs = {
                    "class" : "form-control",
                    "rows" : 3,
                    "cols" : 20
                }
            ),
            "network" : forms.TextInput(
                attrs = {
                    "class" : "form-control"
                }
            ),
            "wifi" : forms.TextInput(
                attrs = {
                    "class" : "form-control"
                }
            ),
            "sim_type" : forms.TextInput(
                attrs = {
                    "class" : "form-control"
                }
            ),
            "color" : forms.TextInput(
                attrs = {
                    "class" : "form-control"
                }
            ),
            "release_date" : forms.DateInput(
                attrs = {
                    "type" : "date",
                    "class" : "form-control"
                }
            )
        }