from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(SingleBed, Double_bed, Customer)
class ViewAdmin(admin.ModelAdmin):
    pass
