from rest_framework import serializers
from django.db.models import Q
from detection.models import Person, Diagnose


class DiagnoseSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='diagnose-detail')
    
    class Meta:
        model = Diagnose
        fields = "__all__"


class PersonListSerializer(serializers.ModelSerializer):
    updated = serializers.SerializerMethodField('get_updated')
    url = serializers.HyperlinkedIdentityField(view_name='detection:detail')

    def get_updated(self, person):
        try:
            qs = Diagnose.objects.filter(person=person)
            latest_diagnose = qs.latest('updated')
        except:
            return None
        return latest_diagnose.updated

    class Meta:
        model = Person
        fields = [
            'id',
            'name',
            'sex',
            'birth',
            'updated',
            'url'
        ]


class PersonDetailSerializer(serializers.ModelSerializer):
    diagnose_set = DiagnoseSerializer(many=True, read_only=True)
    updated = serializers.SerializerMethodField('get_updated')

    def get_updated(self, person):
        try:
            qs = Diagnose.objects.filter(person=person)
            latest_diagnose = qs.latest('updated')
        except:
            return None
        return latest_diagnose.updated

    class Meta:
        model = Person
        fields = [
            'id',
            'name',
            'sex',
            'diagnose_set',
            'birth',
            'updated'
        ]
