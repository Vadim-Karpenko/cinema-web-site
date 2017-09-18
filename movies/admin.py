from django.contrib import admin
from .models import Movie, Places

class MovieAdmin(admin.ModelAdmin):
     prepopulated_fields = {"slug": ("title",)}
     list_display = ['title', 'genre',
                     'duration', 'price',
                     'start_time', 'release_date']
     list_filter = ['release_date', 'start_time']
     search_fields = ['title', 'genre',
                     'duration', 'price',
                     'start_time', 'release_date']

class PlacesAdmin(admin.ModelAdmin):
     fieldsets = [
        ("Related movie", {'fields': ['chain_models']}),
        ("Row 1", {'fields': [('row1_place1', 'row1_place2', 'row1_place3', 'row1_place4', 'row1_place5', 'row1_place6', 'row1_place7', 'row1_place8')]}),
        ("Row 2", {'fields': [('row2_place1', 'row2_place2', 'row2_place3', 'row2_place4', 'row2_place5', 'row2_place6', 'row2_place7', 'row2_place8')]}),
        ("Row 3", {'fields': [('row3_place1', 'row3_place2', 'row3_place3', 'row3_place4', 'row3_place5', 'row3_place6', 'row3_place7', 'row3_place8')]}),
        ("Row 4", {'fields': [('row4_place1', 'row4_place2', 'row4_place3', 'row4_place4', 'row4_place5', 'row4_place6', 'row4_place7', 'row4_place8')]}),
        ("Row 5", {'fields': [('row5_place1', 'row5_place2', 'row5_place3', 'row5_place4', 'row5_place5', 'row5_place6', 'row5_place7', 'row5_place8')]}),
    ]

admin.site.register(Movie, MovieAdmin)
admin.site.register(Places, PlacesAdmin)
