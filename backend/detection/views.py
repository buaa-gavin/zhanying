# Create your views here.
from detection.models import Person, CancerImage
from django.http import JsonResponse
from detection.serializers import PersonListSerializer


def info_list(request):
    info = Person.objects.all()
    serializer = PersonListSerializer(info,many = True)
    return JsonResponse(serializer.data, safe = False)
