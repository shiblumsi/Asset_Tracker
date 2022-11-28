from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

from django.http import Http404
from .models import *
from .serializers import AddEmployeeSerializer,\
    AddAssetSerializer,DelegateToSerializer,\
    WhenGiveAndReturnSerializer,ConditionGiveAndReturnSerializer,UserRegistrationSerializer,\
    UserLoginSerializer




class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
           
            return Response({'message':'Account Created!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

class UserLoginView(APIView):
    def post(self,request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email,password=password)
            
            
            if user is not None:
                return Response({ 'message':'Login Sucess'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or Password not mathed']}},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




class AddEmployeeView(APIView):                 #Adding & Fetching Employee

    def get(self, request):
        snippets = Employee.objects.all()
        serializer = AddEmployeeSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AddEmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AddAssetView(APIView):                    #Adding & Fetching Asset

    def get(self, request):
        asset = Asset.objects.all()
        serializer = AddAssetSerializer(asset,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AddAssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DelegateToView(APIView):                  #Delegate one or more devices to employees
   
    def get(self, request):
        asset = DelegateTo.objects.all()
        serializer = DelegateToSerializer(asset,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DelegateToSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class WhenGiveAndReturnView(APIView):            #see when a Device was checked out and returned
    
    def get_object(self, pk):                    #get a single Object
        try:
            return GiveBack.objects.get(pk=pk)
        except GiveBack.DoesNotExist:
            raise Http404

    def get(self,request,pk):                      
        obj = self.get_object(pk)
        serializer = WhenGiveAndReturnSerializer(obj)
        return Response(serializer.data)



class ConditionGiveAndReturnView(APIView):        #condition it was handed out and returned
   
    def get_object(self, pk):
        try:
            return GiveBack.objects.get(pk=pk)
        except GiveBack.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        condition = self.get_object(pk)
        serializer = ConditionGiveAndReturnSerializer(condition)
        return Response(serializer.data)