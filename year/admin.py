from django.contrib import admin

# Register your models here.
from .models import Test


class TestAdmin(admin.ModelAdmin):
	list_display = [
	'title',
	]


admin.site.register(Test,TestAdmin)