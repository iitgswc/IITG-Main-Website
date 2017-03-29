from django.contrib import admin
from django.contrib.auth.models import * 
from .models import *

# register the sections of the site
admin.site.register(About)
admin.site.register(AcademicAffairs)
admin.site.register(Administration)
admin.site.register(Department)
admin.site.register(AcademicCenter)
admin.site.register(ExtramurailCenter)
admin.site.register(ExchangeProgram)
admin.site.register(Utility)
admin.site.register(Form)
admin.site.register(Partnership)
admin.site.register(CarouselImages)
admin.site.register(Announcement)
admin.site.register(ResearchInnovation)
admin.site.register(UpcomingEvent)
admin.site.register(QuickLink)
admin.site.register(Resource)
admin.site.register(Programm)
admin.site.register(Current)

# unregister the users model
# admin.site.unregister(Group)
# admin.site.unregister(User)