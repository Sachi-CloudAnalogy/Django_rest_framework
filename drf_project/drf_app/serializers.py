from rest_framework import serializers
from .models import Student

#Validators  -- define function name and body yourself
def starts_with_r(value):
    if value['0'].lower != 'r':
        raise serializers.ValidationError('Name should start with R')

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[starts_with_r])
    roll_no = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll_no = validated_data.get('roll_no', instance.roll_no)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    #Validator -- field level validation
    def validate_roll_no(self, value):    #it is invoked automatically when is_valid() method is called
        if value>=200:
            raise serializers.ValidationError("Not allowed")
        return value

    #Object level validation
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')
        if name.lower() == 'kajal' and city.lower() != 'ranchi':
            raise serializers.ValidationError('City must be Ranchi')
        return data

    