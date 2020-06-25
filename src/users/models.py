from django.db import models


class User(models.Model):
    userid = models.CharField(max_length=75)
    realname = models.CharField(max_length=2000)
    tz = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, editable=False)


class ActivityPeriod (models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      start_time = models.DateTimeField()
      end_time = models.DateTimeField()


