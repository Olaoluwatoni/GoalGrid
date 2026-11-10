from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('goals/', views.goals, name='goals'),
    path('goals/add/', views.add_goal, name='add_goal'),
    path('goals/<int:goal_id>/edit/', views.edit_goal, name='edit_goal'),
    path('goals/<int:goal_id>/toggle/', views.toggle_goal, name='toggle_goal'),
    path('goals/<int:goal_id>/delete/', views.delete_goal, name='delete_goal'),
]