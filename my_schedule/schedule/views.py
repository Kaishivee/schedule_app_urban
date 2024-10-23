from django.shortcuts import render, redirect, get_object_or_404
from .models import Lesson, Group
from .forms import LessonForm


def schedule_view(request):
    groups = Group.objects.all()
    selected_group_id = request.GET.get('group')
    if selected_group_id:
        selected_group = get_object_or_404(Group, id=selected_group_id)
    else:
        selected_group = groups.first()  # Выбираем первую группу по умолчанию

    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
    schedule = {}
    for day in days:
        lessons = Lesson.objects.filter(day_of_week=day, group=selected_group).order_by('time')
        schedule[day] = lessons

    context = {
        'schedule': schedule,
        'groups': groups,
        'selected_group': selected_group,
    }
    return render(request, 'schedule/schedule.html', context)


def lesson_create(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule')
    else:
        form = LessonForm()
    return render(request, 'schedule/lesson_form.html', {'form': form})


def lesson_edit(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('schedule')
    else:
        form = LessonForm(instance=lesson)
    return render(request, 'schedule/lesson_form.html', {'form': form})


def lesson_delete(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == 'POST':
        lesson.delete()
        return redirect('schedule')
    return render(request, 'schedule/lesson_confirm_delete.html', {'lesson': lesson})
