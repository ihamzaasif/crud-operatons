from django.contrib.auth.models import User
from django.db import models

class MyUser(User):

    class Meta:
        db_table="user_table"