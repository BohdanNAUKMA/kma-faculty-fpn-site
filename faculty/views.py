from django.shortcuts import render, get_object_or_404
from .models import Department, Program, Teacher, FacultyInfo

# Create your views here.
def home_view(request):
    """Головна сторінка: опис факультету та контакти деканату"""
    faculty_info = FacultyInfo.objects.first()
    return render(request, 'faculty/home.html', {'faculty_info': faculty_info})


def program_list_view(request):
    """Список освітніх програм із коротким описом"""
    programs = Program.objects.select_related('department').all()
    return render(request, 'faculty/programs_list.html', {'programs': programs})


def program_detail_view(request, pk):
    """Детальна сторінка програми з повним описом та переліком дисциплін"""
    program = get_object_or_404(Program, pk=pk)
    # Розбиваємо перелік дисциплін на рядки для зручного виводу
    disciplines_list = [d.strip() for d in program.disciplines.splitlines() if d.strip()]
    return render(request, 'faculty/program_detail.html', {
        'program': program,
        'disciplines_list': disciplines_list
    })


def department_list_view(request):
    """Список кафедр із переліком випускових спеціальностей"""
    departments = Department.objects.prefetch_related('programs').all()
    return render(request, 'faculty/departments_list.html', {'departments': departments})


def department_detail_view(request, pk):
    """Детальна сторінка кафедри зі списком викладачів"""
    department = get_object_or_404(Department, pk=pk)
    teachers = department.teachers.all()
    return render(request, 'faculty/department_detail.html', {
        'department': department,
        'teachers': teachers
    })