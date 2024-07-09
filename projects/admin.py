from django.contrib import admin

# Register your models here.
# projects/admin.py

from projects.models import Project, Person

class ProjectAdmin(admin.ModelAdmin):
    pass

class PersonAdmin(admin.ModelAdmin):
    pass



admin.site.register(Project, ProjectAdmin)
admin.site.register(Person, PersonAdmin)


