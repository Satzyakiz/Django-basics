from django.contrib import admin
from . import models
# Register your models here.
class MovieAdmin(admin.ModelAdmin):

    fields = ['release','title','length'] #arrangement of fields
    search_fields = ['title','length'] #automatically create search_fields
    list_filter = ['title','length','release']
    list_display = ['title','length','release'] #display the mentioned in this order only
    list_editable = ['length','release']

admin.site.register(models.Movie,MovieAdmin)
admin.site.register(models.Customer)
