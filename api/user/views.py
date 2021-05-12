import csv

from user.models import User
from rest_framework import viewsets, generics
from rest_framework import filters
from api.user.serializers import UserSerializer

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
#from rest_framework_jwt.settings import api_settings


from django.http import HttpResponse

from user.models import User


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'email']

class UsersExportAsCSV(generics.ListAPIView):

  def get(self, request, format=None):
    response = HttpResponse(content_type='text/csv')
    filename = u"customer_base_report.csv"
    response['Content-Disposition'] = u'attachment; filename="{0}"'.format(filename)
    writer = csv.writer(
      response,
      delimiter=';',
      quotechar='"',
      quoting=csv.QUOTE_ALL
    )

    for f in User.objects.all():
      writer.writerow([f.email, f.first_name, f.last_name, f.telephone])

    return response