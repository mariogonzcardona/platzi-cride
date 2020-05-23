"""Circles Views"""

# Django REST Framework
from rest_framework.decorators import api_view
from cride.circles.models import Circle
# Models
from rest_framework.response import Response
# Serializer
from cride.circles.serializers import CircleSerializer,CreateCircleSerializer

@api_view(['GET'])
def list_circles(request):
    # Normal form
    # data=[{"name":circle.name,
    #     "slug":circle.slug_name,
    #     "rides_taken":circle.rides_taken,
    #     "rides_offered":circle.rides_offered,
    #     "members_limit":circle.members_limit} for circle in Circle.objects.all().filter(is_public=True)]
    # return Response(data)

    # Serializer 
    # circles=Circle.objects.filter(is_public=True)
    # data=[]
    # for circle in circles:
    #     serializer=CircleSerializer(circle)
    #     data.append(serializer.data)
    # return Response(data)

    # List Comprehensions
    # data=[CircleSerializer(circle).data for circle in Circle.objects.filter(is_public=True)]
    # return Response(data)

    # Complex Serializers
    circle=Circle.objects.filter(is_public=True)
    serializer= CircleSerializer(circle,many=True)
    return Response(serializer.data)




@api_view(['POST'])
def create_circle(request):
    """Create Circle"""
    # name=request.data['name']
    # slug_name=request.data['slug_name']
    # about=request.data.get('about','')
    # circle=Circle.objects.create(name=name,slug_name=slug_name,about=about)

    # data={
    #     "name":circle.name,
    #     "slug":circle.slug_name,
    #     "rides_taken":circle.rides_taken,
    #     "rides_offered":circle.rides_offered,
    #     "members_limit":circle.members_limit,
    # }
    # return Response(data)

    serializer=CreateCircleSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    circle=serializer.save()
    return Response(CircleSerializer(circle).data)
    