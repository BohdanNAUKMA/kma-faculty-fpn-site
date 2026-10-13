from django.contrib import admin

# Register your models here.
from .models import Department, Program, Teacher, FacultyInfo, ExchangeProgram


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "head_name", "programs_count", "teachers_count")
    search_fields = ("name", "head_name")

    @admin.display(description="Кількість програм")
    def programs_count(self, obj):
        return obj.programs.count()

    @admin.display(description="Кількість викладачів")
    def teachers_count(self, obj):
        return obj.teachers.count()


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "department", "coordinator_name", "coordinator_contact")
    list_filter = ("department",)
    search_fields = ("name", "code", "coordinator_name")
    list_select_related = ("department",)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "degree", "department")
    list_filter = ("department", "position")
    search_fields = ("name", "degree")
    list_select_related = ("department",)


@admin.register(FacultyInfo)
class FacultyInfoAdmin(admin.ModelAdmin):
    list_display = ("title",)

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(ExchangeProgram)
class ExchangeProgramAdmin(admin.ModelAdmin):
    list_display = ('university', 'country', 'languages', 'seats', 'deadline')
    list_filter = ('country', 'deadline')
    search_fields = ('university', 'country', 'languages')