from django_filters import rest_framework
from .models import Pereval


class PerevalFilter(rest_framework.FilterSet):
    user__email = rest_framework.CharFilter(field_name='user__email')

    class Meta:
        model = Pereval
        fields = ['user__email', ]
