#import csv

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
#from rest_framework_jwt.settings import api_settings


from django.http import HttpResponse

from user.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'telephone')