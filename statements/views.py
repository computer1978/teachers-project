from django.shortcuts import redirect, render
from .models import Teachers, Leave
from .forms import LeaveForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request, 'index.html')

def teachers_name(request):
    teacher_names = Teachers.objects.all()
    context = {'teacher_names':teacher_names}
    return render(request, 'teachers_name.html', context)

@login_required
def leave(request):
    teacher = Teachers.objects.get(owner=request.user)
    leave = Leave.objects.filter(owner=request.user)
    context = {'leave':leave, 'teacher':teacher}
    return render(request, 'leave.html', context)

@login_required
def add_leave(request):
    #owner = request.user
    #owner_id = owner.id
    #teacher = TeachersName.objects.get(owner_id=owner_id)
    teacher = Teachers.objects.get(owner=request.user)
    if request.method != 'POST':
        form = LeaveForm()

    else:
        form = LeaveForm(data=request.POST)
        if form.is_valid():
            new_leave = form.save(commit=False)
            new_leave.owner = request.user
            new_leave.bfs_task_duration = abs((new_leave.date_of_leave - new_leave.date_of_return).days)
            new_leave.save()
            return redirect('statements:leave')
    context = {'form': form, 'teacher': teacher}
    return render(request, 'add_leave.html', context)

@login_required
def delete_leave(request, leave_id):
    leave = Leave.objects.get(id=leave_id)
    leave.delete()
    return redirect('statements:leave')
