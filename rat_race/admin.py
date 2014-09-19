from django.contrib import admin
from rat_race.models import Runner, Topic, Quiz
# Register your models here.


@admin.register(Runner)
class RunnerAdmin(admin.ModelAdmin):
    pass


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    pass


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass