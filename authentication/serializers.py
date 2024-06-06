from datetime import date
from rest_framework import serializers
from .models import User, Rol


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'


class AgeValidator:
    def __call__(self, value):
        today = date.today()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if age < 18:
            raise serializers.ValidationError("The user must be over 18 years old")


class UserSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(validators=[AgeValidator()])

    class Meta:
        model = User
        fields = [
            'id',
            'full_name',
            'email',
            'phone',
            'birth_date',
            'is_active',
            'is_staff',
            'is_superuser',
            'rol'
        ]
