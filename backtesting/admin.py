from django.contrib import admin

from .models import Tradable, Condition, Price

admin.site.register(Tradable)
admin.site.register(Condition)
admin.site.register(Price)
