from django.contrib import admin
from .models import Service, BasicService, StandardService, PremiumService, ServiceText, FeaturesText, Planstext,Project,ProjectFilter,ProjectText,ProjectPhoto
# Register your models here.
# --------------------- Services admin panel form ----------------------------------->>>
admin.site.register(ServiceText)
admin.site.register(FeaturesText)
admin.site.register(Planstext)


# -----------------------Packages for admin panel form -------------------------------------->
class BasicServiceInline(admin.StackedInline):
    model = BasicService
    extra = 1

class StandardServiceInline(admin.StackedInline):
    model = StandardService
    extra = 1

class PremiumServiceInline(admin.StackedInline):
    model = PremiumService
    extra = 1
# ------------------------Service form ----------------------------------------------------->
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')
    search_fields = ('title',)
    inlines = [BasicServiceInline, StandardServiceInline, PremiumServiceInline]

@admin.register(BasicService)
class BasicServiceAdmin(admin.ModelAdmin):
    list_display = ('iid', 'service_title', 'price')
    search_fields = ('service__title',)

    def service_title(self, obj):
        return obj.service.title
    service_title.short_description = 'Service Title'

@admin.register(StandardService)
class StandardServiceAdmin(admin.ModelAdmin):
    list_display = ('iid', 'service_title', 'price')
    search_fields = ('service__title',)

    def service_title(self, obj):
        return obj.service.title
    service_title.short_description = 'Service Title'

@admin.register(PremiumService)
class PremiumServiceAdmin(admin.ModelAdmin):
    list_display = ('iid', 'service_title', 'price')
    search_fields = ('service__title',)

    def service_title(self, obj):
        return obj.service.title
    service_title.short_description = 'Service Title'

# -----------------------------------------Project forms  for admin panel ------------------------>
admin.site.register(ProjectPhoto)
admin.site.register(ProjectFilter)
admin.site.register(ProjectText)
admin.site.register(Project)