from rest_framework.response import Response
from .serializers import AdSerializer, LocationSerializer
from ..models import Ad, Location
from rest_framework import status, viewsets, generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend 
from ads_system.tasks import ad_run #it's a celery task


#You can perform POST, PUT, DELETE and GET method with this viewset
class AdsViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    #Overriding Post method
    def create(self, request, *args, **kwargs):
        serializer = AdSerializer(data=request.data)

        cities = request.data['cities']
        start_date = request.data['start_date']
        end_date = request.data['end_date']
        visitors_per_day = request.data['visitors_per_day']
        if serializer.is_valid():
            ad_run.delay(cities, start_date, end_date, visitors_per_day)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Endpoint for search ads according to keywords
class AdsFilterView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['keyword']

