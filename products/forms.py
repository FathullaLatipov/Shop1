from django import forms

from products.models import CommentModel


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        exclude = ['post', 'created_at']