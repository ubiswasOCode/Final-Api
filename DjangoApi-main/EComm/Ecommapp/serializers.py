
from unicodedata import category
from rest_framework import serializers
from.models import Product, RegisterUser, Category
from rest_framework_simplejwt.tokens import RefreshToken
import json

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = ["id", "username",  "first_name", "last_name",
                  "gender", "email","age","phone_number" , 'password'
                  ]
        
class UserSerializerWithToken(RegisterSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = RegisterUser
        fields = ["id", "username",  "first_name", "last_name",
                  "gender", "email","age","phone_number" ,"token"
                  ]
    
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        
        return token.access_token        




class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"          
   
class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"          