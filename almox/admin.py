from django.contrib import admin

# Register your models here.
from .models import Loc
from .models import Mod
from .models import Type
from .models import Comp

@admin.register(Loc)
class LocAdmin(admin.ModelAdmin):
    list_display = ('loc_name', 'loc_addrss')

@admin.register(Mod)
class LocAdmin(admin.ModelAdmin):
    list_display = ('mod_brand', 'mod_model')

@admin.register(Type)
class LocAdmin(admin.ModelAdmin):
    list_display = ('type_desc',)

@admin.register(Comp)
class LocAdmin(admin.ModelAdmin):
    list_display = ('comp_name', 'comp_status', 'comp_estado', 'comp_loc')