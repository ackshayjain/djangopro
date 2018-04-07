from django.contrib import admin

# Register your models here.
from .models import Test


# class ComplaintAdmin(admin.ModelAdmin):
# 	list_display = [
# 	'title',
# 	'
# 	]


admin.site.register(Test)