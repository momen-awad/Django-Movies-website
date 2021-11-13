from rest_framework.decorators import api_view
from .serializer import MovieSerializer
from .models import Movie
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

@api_view(['GET'])
def movie_data(request):
    all_movie = Movie.objects.all()
    data = MovieSerializer(all_movie, many=True).data

    return Response({'data': data})


@api_view(['POST'])
def create_movie(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    return Response(data=serializer.data,status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movie_detail(request,id):
    try:
        movie = Movie.objects.get(id=id)
    except Exception as e:
        return Response(data={"message":"Movie doesn't exist"},status=status.HTTP_400_BAD_REQUEST)

    serializer = MovieSerializer(instance=movie)
    return Response(data=serializer.data,status=status.HTTP_200_OK)

@api_view(['Delete'])
def movie_deleted(request,id):
    response = {}
    try:
        movie_delete = Movie.objects.get(id=id)
        movie_delete.delete()
        response['data'] = {"message":'successfully deleted'}
        response['status'] = status.HTTP_200_OK
    except Exception as e :
        response['data'] = {"message":"something wrong happened"}
        response['status'] = status.HTTP_400_BAD_REQUEST

    return Response(**response)


@api_view(['PUT','PATCH'])
def movie_updated(request,id):
    try:
        movie_update = Movie.objects.get(id=id)
    except Exception as e :
        return Response(data={"message":"somthing went wrong "},status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        serializer = MovieSerializer(instance=movie_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = MovieSerializer(instance=movie_update, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    #if serialize.is_valid():
    #    serialize.save()
    #    return Response(data=serialize.data,status=status.HTTP_200_OK)

    #return Response(data=serialize.errors, status=status.HTTP_400_BAD_REQUEST)


#class MovieList(generics.ListCreateAPIView):
#    queryset = Movie.objects.all()
#    serializer_class = MovieSerializer


#class MovieDetails(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Movie.objects.all()
#    serializer_class = MovieSerializer
#    lookup_field = 'id'
