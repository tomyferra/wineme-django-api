from django.contrib import admin
from .models import Wine

class WineAdmin(admin.ModelAdmin):
    list_display = ('Name', 
                    'Winery',
                    'Variety',
                    'Image',
                    'Region',
                    'Description',
                    'Year',
                    'Totalqualifications',
                    'Avgqualifications',
                    'Score'
                    )

# Register your models here.
admin.site.register(Wine, WineAdmin)