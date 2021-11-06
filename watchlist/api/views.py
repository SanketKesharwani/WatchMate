from watchlist.models import Movie
from rest_framework.response import Response
from watchlist.api.serializers import MovieSerializer
from rest_framework.decorators import api_view

@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies,many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view()
def movie_details(request,pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)