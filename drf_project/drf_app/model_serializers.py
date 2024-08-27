from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll_no', 'city'] 
        

# No need of fields description, create or update method
# class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)     #validator  -- we can't update it now

    #Validators  -- define function name and body yourself
    # def starts_with_r(value):
    #     if value['0'].lower != 'r':
    #         raise serializers.ValidationError('Name should start with R')

    # name = serializers.CharField(validators=[starts_with_r])    
    # class Meta:
    #     model = Student
    #     fields = ['id', 'name', 'roll_no', 'city']
        # read_only_fields = ['name', 'roll_no']      #write like this for multiple fields
        # extra_kwargs = {'name': {'read_only': True}}    #another way of writing validators

    # we can create all the 3 types of validators in the same way
    # field level validation
    # def validate_roll_no(self, value):    
    #     if value>=200:
    #         raise serializers.ValidationError("Not allowed")
    #     return value

    #Object level validation
    # def validate(self, data):
    #     name = data.get('name')
    #     city = data.get('city')
    #     if name.lower() == 'kajal' and city.lower() != 'ranchi':
    #         raise serializers.ValidationError('City must be Ranchi')
    #     return data  
          