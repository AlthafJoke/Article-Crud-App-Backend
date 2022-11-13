from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializers, UserSerializer
from django.http import  JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser, json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User



#class based view using ModelViewSet
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer





#class based view with generic viewset
"""
class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    
"""


#class based view using viewset and routed
"""
class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializers(articles, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ArticleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializers(article)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializers(article, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        article = Article.objects.get(pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""       
    
        
        

#class based views 
"""
class ArticleList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    
class ArticleDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    lookup_field = 'id'
    
    def get(self, request, id):
        return self.retrieve(request, id = id)
    
    def put(self, request, id):
        return self.update(request, id=id)
    
    def delete(self, request, id):
        return self.destroy(request, id=id)
"""


#class based views
"""
class ArticleList(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializers(articles, many=True)
        print(articles)
        print(serializer)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ArticleDetails(APIView):
    def get_object(self, id):
        try:
            return Article.objects.get(id=id)
    
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializers(article)
        
        return Response(serializer.data)
    
    def put(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializers(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        
"""
        
        
        
        
            
    
        
        
        
        
        


#funtion based view with decorator
"""
@api_view(['GET', 'POST'])
def article_list(request):
    #get all articles
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializers(articles, many=True)
        print(articles)
        print(serializer)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        
        
        serializer = ArticleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    

@api_view(['GET', 'PUT', 'DELETE'])
def articles_details(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ArticleSerializers(article)
        return  Response(serializer.data)
    
    elif request.method == "PUT":
        
        serializer = ArticleSerializers(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
"""
        
        
        
        
        
        
        
