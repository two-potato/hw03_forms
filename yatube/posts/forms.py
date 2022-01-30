from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['group'].empty_label = "Выберите группу"

    def clean_text(self):
        text = self.cleaned_data['text']
        if text == '':
            raise forms.ValidationError(
                'Эй! Ты ничего не ввел! Давай-ка еще раз!'
            )
        return text
