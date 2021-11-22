from watchlist.models import WatchList,StreamPlatform,Review
from watchlist.api.permissions import AdminOrReadOnly,ReviewUserOrReadOnly
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchlist.api.serializers import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer
from rest_framework import mixins
from rest_framework import generics
    
#----------------------------------------------------------------------------------------
#   class based api views
#-----------------------------------------------------------------------------------------

#USING CONCRETE CLASS VIEW AVOIDS WRITING GET,POST..... REQUEST LIKE IN MIXINS

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self,serializer):
        pk = self.kwargs['pk']
        movie = WatchList.objects.get(pk=pk)
        
        user_review = self.request.user
        review_queryset = Review.objects.filter(watchlist=movie,user_review=user_review)
        
        if review_queryset.exists():
            raise ValidationError("You have already rated this movie!")
        
        if movie.number_rating == 0:
            movie.avg_rating = serializer.validated_data['rating']
        else:
            movie.avg_rating = (movie.avg_rating + serializer.validated_data['rating'])/2
        
        movie.number_rating = movie.number_rating + 1
        movie.save()
        
        serializer.save(watchlist=movie,user_review=user_review)
    

class ReviewList(generics.ListCreateAPIView):
    #this queryset will return all review so if we want reviews perticular to id we need to overwrite queryset
    #queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

#--------------------------------------------------------------------------------------------
# class based api views USING MIXINS AND GENERICAPIVIEW----------------------------------------------------------

# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#---------------------------------------------------------------------------------------------------

class WatchListAV(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class WatchDetailAV(APIView):
    def get(self, request,pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error':"WatchList does not exist"},status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request,pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class StreamPlatformAV(APIView):
    def get(self, request):
       platform = StreamPlatform.objects.all()
       serializer = StreamPlatformSerializer(platform,many=True)
       return Response(serializer.data)
   
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class StreamPlatformDetailAV(APIView):
    def get(self, request,pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error':"WatchList does not exist"},status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)

    def put(self, request,pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#------------------------------------------------------------------------------------------
 


#-------------------------------------------------------------------------------------------
#FUNCTION BASED API VIEW 
#-------------------------------------------------------------------------------------------
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies,many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request,pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error':"Movie does not exist"},status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#----------------------------------------------------------------------------------------------------------