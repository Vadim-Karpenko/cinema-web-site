from django import forms
from django.template.defaultfilters import slugify
from .models import Movie, Places
from sorl.thumbnail import ImageField
import time


class AddFilmForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'description', 'image', 'genre', 'duration', 'price', 'start_time', 'release_date')


    def __init__(self, *args, **kwargs):
        super(AddFilmForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['class'] = 'dropzone'
        self.fields['start_time'].widget.attrs['class'] = 'start_time'
        self.fields['start_time'].widget.attrs['placeholder'] = 'YYYY-MM-DD 00:00:00'
        self.fields['release_date'].widget.attrs['class'] = 'release_date'
        self.fields['release_date'].widget.attrs['placeholder'] = 'YYYY-MM-DD'

class SearchFilmForm(forms.Form):
    search_text = forms.CharField(max_length=60)

class Placeform(forms.ModelForm):

    class Meta:
        model = Places
        fields = ('row1_place1','row1_place2','row1_place3','row1_place4','row1_place5','row1_place6','row1_place7','row1_place8',
                  'row2_place1','row2_place2','row2_place3','row2_place4','row2_place5','row2_place6','row2_place7','row2_place8',
                  'row3_place1','row3_place2','row3_place3','row3_place4','row3_place5','row3_place6','row3_place7','row3_place8',
                  'row4_place1','row4_place2','row4_place3','row4_place4','row4_place5','row4_place6','row4_place7','row4_place8',
                  'row5_place1','row5_place2','row5_place3','row5_place4','row5_place5','row5_place6','row5_place7','row5_place8')
