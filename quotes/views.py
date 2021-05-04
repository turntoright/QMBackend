from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import status, viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.http import Http404
from quotes.utils import create_quote
from django import http

# Create your views here.


# class Quote(viewsets.ModelViewSet):
#     queryset = models.Quote.objects.all()
#     serializer_class = serializers.Quote
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

class QuoteList(APIView):

    def get(self, request, format=None):
        quotes = models.Quote.objects.all()
        quote_status = self.request.query_params.get('status')
        if quote_status:
            quotes = quotes.filter(status=quote_status)
        serializer = serializers.QuoteSerializer(quotes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.QuoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuoteDetail(APIView):

    def get_object(self, pk):
        try:
            return models.Quote.objects.get(pk=pk)
        except models.Quote.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        quote = self.get_object(pk)
        serializer = serializers.QuoteSerializer(quote)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        quote = self.get_object(pk)
        serializer = serializers.QuoteSerializer(quote, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        quote = self.get_object(pk)
        quote.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = models.Quote.objects.all()
    serializer_class = serializers.QuoteSerializer

    def create(self, request, *args, **kwargs):
        items = request.data['items']
        print(items, request.data)
        try:
            quote: models.Quote = create_quote(request=request, items=items)
        except Exception as error:
            return http.JsonResponse({'success': False,
                                      'message': error
                                      })

        queryset = models.Quote.objects.get(pk=quote.id)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = models.Quote.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = models.Quote.objects.get(id=pk)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        queryset = models.Quote.objects.get(id=pk)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)