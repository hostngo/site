from django.contrib import admin

from .models import CertificateModel, WorkModel


@admin.register(CertificateModel)
class CertificateModelAdmin(admin.ModelAdmin):
    '''Admin View for CertificateModel'''

    list_display = ('certificate_image', )


@admin.register(WorkModel)
class WorkModelAdmin(admin.ModelAdmin):
    '''Admin View for WorkModel'''

    list_display = ('work_image', )
