from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import F
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .forms import GoalForm
from .models import Goal


def index(request):
    return render(request, 'tracker/index.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/signup.html', {'form': form})


@login_required
def goals(request):
    user_goals = Goal.objects.filter(user=request.user).order_by(
        'completed',
        F('due_date').asc(nulls_last=True),
        '-created_at',
    )
    return render(request, 'tracker/goals.html', {
        'goals': user_goals,
        'total': user_goals.count(),
        'completed': user_goals.filter(completed=True).count(),
        'today': timezone.localdate(),
    })


@login_required
def add_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('goals')
    else:
        form = GoalForm()
    return render(request, 'tracker/add_goal.html', {'form': form})


@login_required
def edit_goal(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id, user=request.user)
    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('goals')
    else:
        form = GoalForm(instance=goal)
    return render(request, 'tracker/edit_goal.html', {'form': form})


@login_required
@require_POST
def toggle_goal(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id, user=request.user)
    goal.completed = not goal.completed
    goal.save()
    return redirect('goals')


@login_required
@require_POST
def delete_goal(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id, user=request.user)
    goal.delete()
    return redirect('goals')