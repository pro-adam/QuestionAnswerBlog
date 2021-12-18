from django.contrib import admin
from . models import Question,Answer,DownVote,UpVote,Comment

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title','user')
    search_fields = ['title','detail']
admin.site.register(Question,QuestionAdmin)

admin.site.register(Answer)
admin.site.register(DownVote)
admin.site.register(UpVote)
admin.site.register(Comment)
