from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class userserializer(serializers.ModelSerializer):
   class Meta:
      model=User
      fields=['username','password']
   def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class serializerfreak(serializers.ModelSerializer):
    class Meta:
        model = Freak
        fields = '__all__'

    def validate (self , data):
        if data['name']:
           for n in data['name']:
              if n.isdigit():
               raise serializers.ValidationError({'error':'name cannot be a number'})
        return data

class categoryserializer(serializers.ModelSerializer):
   class Meta:
      model= Category
      fields=['category_name']

class bookserializer(serializers.ModelSerializer):
   class Meta:
      model= book
      fields='__all__'
      depth = 1