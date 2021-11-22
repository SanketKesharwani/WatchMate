from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={input: 'password'},write_only=True)
    
    class Meta:
        model = User
        fields = ['username','email','password','password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def save(self):
        
        password1 = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password1 != password2:
            raise serializers.ValidationError({'error':'Invalid password'})
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'email already exists'})
        
        account = User(username=self.validated_data['username'],email=self.validated_data['email'])
        account.set_password(password1)
        account.save()
        
        return account