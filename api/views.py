from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import offcampus
from . serializers import offcampusSerializer


class offcampusList(APIView):

    def get(self,request,*args,**kwargs):
        company=offcampus.objects.all()
        serializer=offcampusSerializer(company,many=True)
        return Response(serializer.data)
     

    def post(self,request,*args,**kwargs):
        serializer=offcampusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


