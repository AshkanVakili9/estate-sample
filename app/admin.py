from django.contrib import admin
from .models import *




# class UtilityInline(admin.TabularInline):  # یا admin.StackedInline برای نمایش متفاوت
#     model = Utility
#     extra = 1  

# # ثبت مدل PropertySpecification در ادمین به همراه Utility
# @admin.register(PropertySpecification)
# class PropertySpecificationAdmin(admin.ModelAdmin):
#     inlines = [UtilityInline]


admin.site.register(Cartext)

admin.site.register(PropertySpecification)
admin.site.register(PropertyLocation)
admin.site.register(PropertyImage)
admin.site.register(RegistrationInfo)
admin.site.register(Ownership)
admin.site.register(Utility)
admin.site.register(Transaction)
admin.site.register(TechnicalInfo)
