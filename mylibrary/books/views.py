from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .models import Book, Genre
from .serializers import BookSerializer, GenreSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_books(request):
    books = Book.objects.all()

    serializer = BookSerializer(books, many=True)
    ##return JsonResponse(serializer.data, safe=False)
    return render (request, 'books/book_list.html', {'books': books})


@api_view(['POST'])
def create_book(request):
    
    serializer = BookSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['PUT'])
def update_book(request, pk):

    book= Book.objects.get(id=pk)

    serializer = BookSerializer(instance=book, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@api_view(['DELETE'])

def delete_book(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()

    return JsonResponse('Book was deleted successfully', status=204, safe=False)