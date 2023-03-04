from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Member
from datetime import datetime

class CustomDateSerializer(serializers.DateField):
    def to_representation(self, value):
        # Convert the date object to a string in the desired format
        date_str = datetime.strftime(value, '%B %d %Y')
        return date_str

class MemberSerializer(ModelSerializer):
    # dob = CustomDateSerializer()
    class Meta:
        model = Member
        fields = '__all__'