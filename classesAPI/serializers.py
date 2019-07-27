from rest_framework import serializers
from classes.models import Classroom
from django.contrib.auth.models import User


class ClassListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['subject', 'year', 'teacher']

class ClassDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		exclude = ['teacher']

class ClassUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User 
		fields = ['username' , 'password', 'first_name', 'last_name']

		def create(self, validated_data):
			username = validated_data['username']
			password = validated_data['password']
			first_name = validated_data['first_name']
			last_name = validated_data['last_name']
			new_user = User(username=username, first_name=first_name, last_name=last_name)
			new_user.set_password(password)
			new_user.save()
			return validated_data

# class LoginSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = User

# 		def validate(self, data):
# 			my_username = data.get('username')
# 			my_password = data.get('password')


