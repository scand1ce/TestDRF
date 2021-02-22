from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Box, Item, Discr
from .serializers import BoxSerializer, ItemSerializer, CharacteristicsSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'ListBox': '/api/v1/boxes/',
        'CRUDBox': '/api/v1/boxes/<int:pk>',
        'ListItem': '/api/v1/items/',
        'CRUDItem': '/api/v1/items/<int:pk>',
        'ListDescription': '/api/v1/descriptions/',
        'CRUDDescription': '/api/v1/descriptions/<int:pk>',
        'SWAGGER': '/api/v1/swagger/'
    }
    return Response(api_urls)


# class BoxView(generics.ListCreateAPIView):
#     queryset = Box.objects.all()
#     serializer_class = BoxSerializer
#
#
# class BoxDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Box.objects.all()
#     serializer_class = BoxSerializer


class DiscrViewSet(viewsets.ModelViewSet):
    queryset = Discr.objects.all()
    serializer_class = CharacteristicsSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
