from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    tags = models.CharField(max_length=20,default='')
    detail = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    detail = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detail

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_user')
    comment = models.TextField(default='')
    answer  = models.ForeignKey(Answer,on_delete=models.CASCADE,related_name='comment_answer')
    created_date = models.DateTimeField(auto_now_add=True)


class UpVote(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='upvote_user')
    answer  = models.ForeignKey(Answer,on_delete=models.CASCADE,related_name='upvote_answer')

class DownVote(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='downvote_user')
    answer  = models.ForeignKey(Answer,on_delete=models.CASCADE,related_name='downvote_answer')
