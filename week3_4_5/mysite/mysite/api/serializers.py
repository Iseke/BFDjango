from rest_framework import serializers
from mysite.api.models import MyUser


class MyUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    role = serializers.IntegerField(required=True)
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(required=True)

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'role')

    def validate_password(self, pswd):
        if len(pswd) < 5:
            raise serializers.ValidationError('Password length should be more than 5')
        return pswd