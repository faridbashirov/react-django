from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,CreateAPIView
from core.models import *
from core.api.serializer import *

import django_filters.rest_framework
class ServiceListView(ListAPIView):
    model=Service
    serializer_class=ServiceSerializer
    queryset=Service.objects.all()
class ServiceDetailView(RetrieveUpdateAPIView):
    model=Service
    serializer_class=ServiceSerializer
    lookup_field="slug"
    queryset=Service.objects.all()

class ContactsView(CreateAPIView):
    model = Contact
    serializer_class=ContactSerializer
    queryset=Contact.objects.all()

class BlogsListView(ListAPIView):
    model=Blogs
    serializer_class=BlogSerializer
    queryset=Blogs.objects.all()

class BlogDetailView(RetrieveUpdateAPIView):
    model=Blogs
    serializer_class=BlogSerializer
    lookup_field="slug"
    queryset=Blogs.objects.all()
class ClientTicketView(RetrieveUpdateAPIView):
    model=Client
    serializer_class=ClientSerializer
    lookup_field="ticket"
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields = ['ticket']   
    queryset=Client.objects.all()

class DeviceGetSerializerView(ListAPIView):
   serializer_class=RepairChoicesSerializer
   queryset=RepairChoices.objects.all()
   filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
   filterset_fields=["device__name"]

class DeviceListView(ListAPIView):
   serializer_class=DeviceSerializer
   queryset=Device.objects.all()
class EstimateCreateView(CreateAPIView):
   model=Estimate
   serializer_class=EstimateSerializer
   queryset=Estimate.objects.all()
   