from django.contrib import admin
from django import forms
from .models import OppositeWord

class MultiOppositeWordForm(forms.ModelForm):
    word_0 = forms.CharField(required=False)
    opposite_0 = forms.CharField(required=False)
    word_1 = forms.CharField(required=False)
    opposite_1 = forms.CharField(required=False)
    word_2 = forms.CharField(required=False)
    opposite_2 = forms.CharField(required=False)
    word_3 = forms.CharField(required=False)
    opposite_3 = forms.CharField(required=False)
    word_4 = forms.CharField(required=False)
    opposite_4 = forms.CharField(required=False)
    word_5 = forms.CharField(required=False)
    opposite_5 = forms.CharField(required=False)
    word_6 = forms.CharField(required=False)
    opposite_6 = forms.CharField(required=False)
    word_7 = forms.CharField(required=False)
    opposite_7 = forms.CharField(required=False)
    word_8 = forms.CharField(required=False)
    opposite_8 = forms.CharField(required=False)
    word_9 = forms.CharField(required=False)
    opposite_9 = forms.CharField(required=False)

    class Meta:
        model = OppositeWord
        fields = []

class OppositeWordAdmin(admin.ModelAdmin):
    form = MultiOppositeWordForm

    # Override save_model method to handle saving multiple records
    def save_model(self, request, obj, form, change):
        for i in range(10):
            word = form.cleaned_data.get(f'word_{i}')
            opposite = form.cleaned_data.get(f'opposite_{i}')
            if word and opposite:
                OppositeWord.objects.create(word=word, opposite=opposite)

    # Override get_fields method to specify fields for the admin form
    def get_fields(self, request, obj=None):
        fields = []
        for i in range(10):  # Assuming you have 10 additional fields initially
            fields.append(f'word_{i}')
            fields.append(f'opposite_{i}')
        return fields

admin.site.register(OppositeWord, OppositeWordAdmin)
