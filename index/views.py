from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from index.serializers import *
from index.models import *
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView


class tokenAU(APIView):
         def post(self, request):
             serializer = userserializer(data = request.data)
             if not serializer.is_valid():
              return Response({'status':403,'errors':serializer.errors,'message':'Something went wrong !'})
             serializer.save()
             user =User.objects.get(username=serializer.data['username'])
             token_obj , _ = Token.objects.get_or_create(user=user)
             return Response({'status':200, 'payload':serializer.data,'token':str(token_obj), 'message':'hello there !'})

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentAPI(APIView):
     authentication_classes=[TokenAuthentication]
     permission_classes=[IsAuthenticated]
     
     def get(self, request):
         freak = Freak.objects.all()
         Serializeraf = serializerfreak(freak, many=True)
         return Response({'status':200,'payload':Serializeraf.data,'message':'requests as given !' })
     
     def post(self, request):
             serializer = serializerfreak(data = request.data)
             if not serializer.is_valid():
              return Response({'status':403,'errors':serializer.errors,'message':'Something went wrong !'})
             serializer.save()
             return Response({'status':200, 'payload':serializer.data, 'message':'hello there !'})
     

     
     def patch(self, request):
             freakti = Freak.objects.get(id=id)
             serializer = serializerfreak(freakti, data = request.data, partial=True)
             if not serializer.is_valid():
              return Response({'status':403,'errors':serializer.errors,'message':'Something went wrong !'})
             serializer.save()
             return Response({'status':200, 'payload':serializer.data, 'message':'hello there !'})
     
     def delete(self, request):
        freakti = Freak.objects.get(id=id)
        freakti.delete()
        return Response({'status':403,'message':'deleted !'})
          

@api_view(['GET'])
def index_new(request):
    books = book.objects.all()
    booksaf = bookserializer(books, many=True)
    return Response({'status':200,'payload':booksaf.data,'message':'requests as given !' })


