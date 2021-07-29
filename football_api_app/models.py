from django.db import models

from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

# Create your models here.

class Football(models.Model):
    player_name = models.CharField(max_length=64)
    position = models.TextField(default="", null=True, blank=True)
    manager = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    player_price = models.JSONField(default=list, blank=True)
    minimum_goal_per_hour = models.IntegerField(default=0)
    maximum_goal_per_hour = models.IntegerField(default=0)
    average_goal_per_year = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.player_name