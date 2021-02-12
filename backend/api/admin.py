from django.contrib import admin

from api.models import User, Place, Topic, Event, EventFilter

admin.site.register(User)
admin.site.register(Place)
admin.site.register(Topic)
admin.site.register(Event)
admin.site.register(EventFilter)
