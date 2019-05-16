
from django.db import models
from datetime import datetime
from django.db import models

#CASCADE means that the row will be deleted too if the ForeignKey gets deleted.


class Project(models.Model):
    project_name = models.CharField(max_length=1000)
    project_description = models.CharField(max_length=1000)
    project_random_phrase = models.CharField(max_length = 255)
    project_editable = models.BooleanField()

class Quest(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    quest_name = models.CharField(max_length=250)
    quest_description = models.CharField(max_length=1000, blank=True, null=True)
    quest_points_earned = models.IntegerField()
    deleted = models.BooleanField(default=False)
    time_modified = models.DateTimeField(auto_now=True)
    #Path number determines the order that you want quests to be accessed
    quest_path_number = models.IntegerField()

   
class Question(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=1000, blank=True, null=True)
    question_type = models.CharField(max_length=45)
    deleted = models.BooleanField(default=False)
    time_modified = models.DateTimeField(auto_now=True)

class IncorrectAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=1000)
    deleted = models.BooleanField(default=False)
    time_modified = models.DateTimeField(auto_now=True)


  
class User(models.Model):
    #Figure out if this on cascade is correct
   user_ldap = models.CharField(max_length=45)
   user_first_name = models.CharField(max_length=45)
   user_last_name = models.CharField(max_length=45)
   user_email = models.CharField(max_length=45)
#    user_manager_ldap = models.CharField(max_length=45)
#    user_director_ldap = models.CharField(max_length=45)
   user_password = models.CharField(max_length = 45)
   user_reset_password_pin = models.CharField(max_length = 5, null=True, default = None)
   #exempt = models.BooleanField(default=False) (This should go in User_project)

   
class CorrectAnswer(models.Model):
   question = models.ForeignKey(Question, on_delete=models.CASCADE)
   answer_text = models.CharField(max_length=1000)
   deleted = models.BooleanField(default=False)
   time_modified = models.DateTimeField(auto_now=True)

  
class CompletedQuest(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
   points_earned = models.IntegerField()
   date_completed = models.DateTimeField()

class CorrectlyAnsweredQuestion (models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class UserProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    #Fix what happens if a single quest gets deleted
    current_quest = models.ForeignKey(Quest, on_delete=models.CASCADE, null=True)
    points = models.IntegerField(default = 0)
    completed_project = models.BooleanField(default=False)
    

class Video(models.Model):
    VIDEO_TYPES = (
    ('Youtube', 'Youtube'),
    ('Personal', 'Personal'))
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    video_url = models.CharField(max_length = 1000)
    video_type = models.CharField(max_length = 1000, choices = VIDEO_TYPES)


class Admin(models.Model):
    admin_ldap = models.CharField(max_length=45)
    admin_first_name = models.CharField(max_length=45)
    admin_last_name = models.CharField(max_length=45)
    admin_email = models.CharField(max_length=45)
    admin_password = models.CharField(max_length = 45)
    admin_reset_password_pin = models.CharField(max_length = 5, null=True)


class AdminProject(models.Model):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)





    
