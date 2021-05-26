# Create your views here.
from rest_framework.response import Response

from detection.models import Person
from detection.serializers import PersonListSerializer


def info_list(request):
    info = Person.objects.all()
    serializer = PersonListSerializer(info, many=True)
    return Response(serializer.data, safe=False)


def info_detail(request, id):
    info = Person.objects.get(id=id)
    diagnose_set = info.diagnose_set.all()
