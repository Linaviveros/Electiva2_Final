from django.urls import path
from . import views

urlpatterns = [
    path('pills/', views.PillListCreate.as_view(), name='pill-list-create'),
    path('reminders/', views.ReminderListCreate.as_view(), name='reminder-list-create'),
    path('check-reminders/', views.CheckReminder.as_view(), name='check-reminders'),
]
