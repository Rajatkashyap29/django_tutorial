from django.contrib import admin
from .models  import chaivarity,Store,chaiReview,chaiCertificate

# Register your models here.


class ChaiReveiwInline(admin.TabularInline):
    model=chaiReview
    extra =2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display= ('name','type','date_added')
    inlines=[ChaiReveiwInline]

class StoreAdmin(admin.ModelAdmin):
    list_display= ('Name','location')   
    filter_horizontal=('chai_varieties',)   

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display=('chai','certificate_number')     

admin.site.register(chaivarity,ChaiVarietyAdmin),
admin.site.register(Store,StoreAdmin),
admin.site.register(chaiCertificate,ChaiCertificateAdmin),