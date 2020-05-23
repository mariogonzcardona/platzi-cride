"""Circles Views"""

from django.http import JsonResponse
from cride.circles.models import Circle
import pprint

def list_circles(request):

    data=[{"name":circle.name,
        "slug":circle.slug_name,
        "rides_taken":circle.rides_taken,
        "rides_offered":circle.rides_offered,
        "members_limit":circle.members_limit} for circle in Circle.objects.all().filter(is_public=True)]
    # pprint.pprint(data)
    return JsonResponse(data,safe=False)


    