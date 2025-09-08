from django import forms 
from .models import ReviewModel

class ReviewForm(forms.ModelForm):

    

    class Meta:
        model = ReviewModel
        fields = ["comment"]
        widgets = {
            "comment" : forms.Textarea(
                attrs = {
                    "class" : "form-control mb-3 border border-2",
                    "placeholder" : "Leave a Write to express your experience",
                    "style" : "resize: none",
                }
            )
        }
