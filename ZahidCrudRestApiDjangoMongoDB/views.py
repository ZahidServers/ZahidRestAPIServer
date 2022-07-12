from django.shortcuts import render
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from ZahidCrudRestApiDjangoMongoDB.models import movie
from ZahidCrudRestApiDjangoMongoDB.serializers import movieSerializer
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def movie_list(request):
	if request.method == 'GET':
		movies = movie.objects.all()
		name = request.GET.get('name', None)
		if name is not None:
			movies = movies.filter(name__icontains=title)
		movies_serializer = movieSerializer(movies, many=True)
		return JsonResponse(movies_serializer.data, safe=False)
		# 'safe=False' for objects serialization
	elif request.method == 'POST':
		movie_data = JSONParser().parse(request)
		movie_serializer = movieSerializer(data=movie_data)
		if movie_serializer.is_valid():
			movie_serializer.save()
			return JsonResponse(movie_serializer.data, status=status.HTTP_201_CREATED) 
		return JsonResponse(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		count = movie.objects.all().delete()
		return JsonResponse({'message': '{} movies were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
	try: 
		moviesf = movie.objects.get(pk=pk) 
	except moviesf.DoesNotExist: 
		return JsonResponse({'message': 'The movie does not exist'}, status=status.HTTP_404_NOT_FOUND)
	if request.method == 'GET': 
		movie_serializer = movieSerializer(moviesf) 
		return JsonResponse(movie_serializer.data)
	elif request.method == 'PUT': 
		movie_data = JSONParser().parse(request) 
		movie_serializer = movieSerializer(moviesf, data=movie_data) 
		if movie_serializer.is_valid(): 
			movie_serializer.save() 
			return JsonResponse(movie_serializer.data) 
		return JsonResponse(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE': 
		moviesf.delete() 
		return JsonResponse({'message': 'movie was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)