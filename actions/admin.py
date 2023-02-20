from django.contrib import admin
from .models import *

class KnightAdmin(admin.ModelAdmin):
    list_display = ['id', 'damage', 'lives', 'alive', 'sword']

class ArcherAdmin(admin.ModelAdmin):
    list_display = ['id', 'damage', 'lives', 'alive', 'sword']

class CatapultAdmin(admin.ModelAdmin):
    list_display = ['id', 'damage', 'lives', 'alive']

class ArmyAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_knights', 'get_archers', 'get_catapults', 'id_army_added']

    def get_knights(self, obj):
        return obj.knights.all().count()

    def get_archers(self, obj):
        return obj.archers.all().count()

    def get_catapults(self, obj):
        return obj.catapults.all().count()

    def id_army_added(self, obj):
        return obj.armyAdd_id

admin.site.register(Knight, KnightAdmin)
admin.site.register(Archer, ArcherAdmin)
admin.site.register(Catapult, CatapultAdmin)
admin.site.register(Army, ArmyAdmin)

