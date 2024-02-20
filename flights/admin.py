from django.contrib import admin
from .models import Flight,Airport,Passenger

class FLightAdmin(admin.ModelAdmin):
    list_display=('id','origin','destination','duration')

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal=('flights',)

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight,FLightAdmin)
admin.site.register(Passenger,PassengerAdmin)
