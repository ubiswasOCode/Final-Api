from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from.serializers import RegisterSerializer, UserSerializerWithToken, productSerializer, categorySerializer
from.models import Product, RegisterUser, Category
# Create your views here.

# Get User


@api_view(['GET'])
def getuser(request):
    user = RegisterUser.objects.all()
    serializer = RegisterSerializer(user, many=True)
    return Response(serializer.data)


# For login Token
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# # Create User
@api_view(['POST'])
def createuser(request):
    data = request.data
    # print(data, "00000000")
    user = RegisterUser.objects.create(
        first_name=data['first_name'],
        last_name=data['last_name'],
        gender=data['gender'],
        username=data['username'],
        email=data['email'],
        age=data['age'],
        phone_number=data['phone_number'],
        password=make_password(data['password']),


    )

    serializer = RegisterSerializer(user)
    return Response(serializer.data)


# Delete user
@api_view(['DELETE'])
def deleteUser(request, pk):
    userForDeletion = RegisterUser.objects.get(id=pk)
    # permission_classes=[IsAuthenticated]
    userForDeletion.delete()
    return Response('User was deleted')


def save(self):
    raise NotImplementedError(
        "Django doesn't provide a DB representation for AnonymousUser.")


# Update user
@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def updateuser(request, pk):
    user = RegisterUser.objects.get(pk=pk)
    # print(request.user)
    #
    data = request.data
    print(data)
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    # user.username = data['email']
    user.email = data['email']
    user.age = data['age']
    user.phone_number = data['phone_number']
    user.gender = data['gender']

    if data['password'] != '':
        user.password = make_password(data['password'])

    user.save()
    serializer = RegisterSerializer(user)
    return Response(serializer.data)


# Create Product
@api_view(['POST'])
def createproduct(request):
    data = request.data
    category = get_object_or_404(Category, id=data['category'])
    product = Product.objects.create(
        category=category,
        brand=data['brand'],
        description=data['description'],
        price=data['price'],
        name=data['name'],
    )

    serializer = productSerializer(product, many=False)
    return Response(serializer.data)


# Get Product

@api_view(['GET'])
def getproduct(request):
    products = Product.objects.all()
    serializer = productSerializer(products, many=True)
    return Response(serializer.data)


# Delete Product
@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def deleteproduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('Product was deleted')


# Update Product
@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def updateproduct(request, pk):
    # print(request,"data__________-")
    updateproducts = Product.objects.get(id=pk)
    data = request.data
    category = Category.objects.get(category=pk)
    # updateproducts.category = data['category']
    updateproducts.name = data['name']
    updateproducts.brand = data['brand']
    updateproducts.description = data['description']
    updateproducts.price = data['price']
    print(updateproducts, "data__________----")

    updateproducts.save()
    serializer = productSerializer(updateproducts)
    print(serializer, "data__________-")

    return Response(serializer.data)


# Create Category
@api_view(['POST'])
def createcategory(request):
    data = request.data
    category = Category.objects.create(
        name=data['name'],
    )
    serializer = categorySerializer(category, many=False)
    return Response(serializer.data)

# get Category


@api_view(['GET'])
def getcategory(request):
    category = Category.objects.all()
    serializer = categorySerializer(category, many=True)
    return Response(serializer.data)


# delete Category
@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return Response('Category Delete')


# Update Category
@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def updatecategory(request, pk):
    updatecategory1 = Category.objects.get(pk=pk)
    data = request.data
    updatecategory1.name = data['name']
    print(updatecategory1, "data__________-")
    # serializer=categorySerializer(updatecategory1)
    # return Response('Category Updated')
    updatecategory1.save()
    serializer = categorySerializer(updatecategory1)

    return Response(serializer.data)
