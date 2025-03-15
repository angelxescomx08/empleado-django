from django.contrib import admin

from .models import Empleado, Habilidades

# Register your models here.
admin.site.register(Habilidades)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "job", "departament", "full_name")
    search_fields = ("first_name",)
    list_filter = ("job", "habilidades")
    filter_horizontal = ("habilidades",)

    def full_name(self, obj):
        return obj.first_name + " " + obj.last_name


admin.site.register(Empleado, EmpleadoAdmin)
