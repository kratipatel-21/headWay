from django.contrib import admin
from Wayahead.models import*

# Register your models here.
@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['topic','desc']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question','topic','difficulty']


    