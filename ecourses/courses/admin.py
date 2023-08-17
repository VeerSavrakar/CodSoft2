from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from courses.models import Course, Learning, Tag, Prerequisite, Vedio, Customuser,UserCourse,Payment

# Register your models here.
class TagAdmin(admin.TabularInline):
    model = Tag

class LearningAdmin(admin.TabularInline):
    model = Learning

class VedioAdmin(admin.TabularInline):
    model = Vedio

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class CustomUserAdmin(UserAdmin):
    # Add any customizations you want for the CustomUser admin here
    pass

class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, LearningAdmin, PrerequisiteAdmin, VedioAdmin]

admin.site.register(Course, CourseAdmin)
# admin.site.register(CustomUser, CustomUserAdmin)  # Register CustomUser with CustomUserAdmin
# admin.site.unregister(CustomUser)  # Unregister the default User model

admin.site.register(Vedio)
admin.site.register(Customuser)
admin.site.register(Payment)
admin.site.register(UserCourse)
