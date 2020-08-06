from django.db import models

class Word(models.Model):
    """
    global unique word
    """
    language = models.CharField(max_length=2, db_index=True)
    meaning = models.TextField()   # json, from web



class UserWord(models.Model):
    """
    one user <-> many words
    """
    user_vid = models.UUIDField(db_index=True)      # onwer user's vid
    circle_stage = models.IntegerField()
    last_op_time = models.IntegerField()            # timestamp, last op: add, remember, forget
    word_id = models.IntegerField()                 # foreign key


class Circle(models.Model):
    """
    one user <-> one circle
    """
    user_vid = models.UUIDField(db_index=True)  # onwer user's vid
    stage1 = models.IntegerField()              # second
    stage2 = models.IntegerField()
    stage3 = models.IntegerField()
    stage4 = models.IntegerField()
    stage5 = models.IntegerField()
    stage6 = models.IntegerField()
    stage7 = models.IntegerField()
    stage8 = models.IntegerField()
    stage_long = models.IntegerField()  # rezo means no long term recycle
    forget_time = models.IntegerField() # words after forget repop
