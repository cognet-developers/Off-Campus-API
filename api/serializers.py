from rest_framework import serializers
from . models import offcampus

class offcampusSerializer(serializers.ModelSerializer):

    class Meta:
        model=offcampus
        fields=(
            'companyname','location','Time','Date','Package','vacancy','Post'
            )
    