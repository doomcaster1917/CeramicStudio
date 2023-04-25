from django.contrib import admin

from django.contrib import admin
from .models import WorkingHours, OurWorks, PhoneNumber, ServicesAndPrices

admin.site.register(OurWorks)
admin.site.register(PhoneNumber)
admin.site.register(ServicesAndPrices)

@admin.register(WorkingHours)
class AuthorAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False