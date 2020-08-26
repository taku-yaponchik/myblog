from django.forms import ModelForm
from django import forms
from .models import Comment, Tag


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs = {'class': "form-control",
                                             'id': "name",
                                             'placeholder': 'Имя'}),
            'body': forms.Textarea(attrs = {'id': "message",
                                            'cols': "30",
                                            'rows': "10",
                                            'class': "form-control",
                                            'placeholder': 'Комментария'})

        }


# def tag_detail(request):
#     tags = Tag.objects.all()
#     return render()

class TagForm(forms.Form):
    title = forms.CharField(max_length = 50)
    slug = forms.CharField(max_length = 50)

    def save(self):
        new_tag = Tag.objects.create(
                title=self.cleaned_data['name'],
                slug=self.cleaned_data['slug']
        )
        return new_tag