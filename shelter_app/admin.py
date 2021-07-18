from django.contrib import admin
from .models import Treatment, VeterinaryTreatment
from . import models

admin.site.register(Treatment)
admin.site.register(VeterinaryTreatment)
admin.site.site_header = 'Schronisko - panel administratora'


class AdmissionInline(admin.TabularInline):
    model = models.Admission
    fields = ['admission_date', 'a_name', 'a_address', 'a_subject']
    extra = 1
    max_num = 1


class OutcomeInline(admin.TabularInline):
    model = models.Outcome
    fields = ['type', 'outcome_date', 'o_name', 'o_address', 'subject_type']
    extra = 1
    max_num = 1


@admin.register(models.Animal)
class AnimalAdmin(admin.ModelAdmin):
    inlines = [AdmissionInline, OutcomeInline]
    search_fields = ['admission_date', 'a_name', 'a_address', 'a_subject', 'type', 'outcome_date', 'o_name', 'o_address', 'subject_type']
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        obj.save()
