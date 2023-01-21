from django.contrib import admin
from .models import Category, Videos_Posted, Profile, Subscribers, Comments

# Register your models here.
admin.site.register(Category)
admin.site.register(Videos_Posted)
admin.site.register(Profile)
admin.site.register(Subscribers)
admin.site.register(Comments)
