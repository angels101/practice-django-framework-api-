from django import forms
from .models import Post,Review,Profile,Rating, RATE_CHOICES
from django.contrib.auth.models import User


 class UploadForm(forms.ModelForm):
     class Meta:
        model = Rating
        fields = ('design','usability','content')

class RateForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea)
    design = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(attrs={'placeholder': 'design'}),required=True)
    usability = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(),required=True)
    content = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(),required=True)

    class Meta:
        model = Review
        fields = ('review','design','usability','content')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'title', 'url', 'description', 'category')


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'photo', 'bio']