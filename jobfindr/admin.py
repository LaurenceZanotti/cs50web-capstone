from django.contrib import admin
from jobfindr.models import User, Profile, Skill

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass

class ProfileAdmin(admin.ModelAdmin):
    pass

class SkillAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)