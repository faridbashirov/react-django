from rest_framework import serializers

from core.models import *

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ('id', 'name', 'small_description', 'icon', 'image', 'slug', 'meta_title', 'meta_description')
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields = ('name', 'email', 'message')

        extra_kwargs = {
            'name': {'error_messages': {'blank': "Please enter a name"}},
            
            'message': {'error_messages': {'blank': "Please write your message"}},
        }
class EstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estimate
        fields = ('first_name', 'last_name', 'phone','email','device_type','repair_type',"message")

        extra_kwargs = {
            'first_name': {'error_messages': {'blank': "Please enter a name"}},
            
            'last_name': {'error_messages': {'blank': "Please write your Last Name"}},
            'phone': {'error_messages': {'blank': "Please write your Phone Number"}},
            'email': {'error_messages': {'blank': "Please write your Email"}},
            'device_type': {'error_messages': {'blank': "Please check your Device Type"}},
            'repair_type': {'error_messages': {'blank': "Please  check your Repair Type "}},
            'message': {'error_messages': {'blank': "Please write your message"}},
        }
class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blogs
        fields = ( 'title', 'description', 'image','slug','small_description','category','meta_title','meta_title','meta_description','meta_keywords',)
class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ( 'first_name', 'last_name','ticket')

class RepairChoicesSerializer(serializers.ModelSerializer):
    device=serializers.SerializerMethodField()
    class Meta:
        model=RepairChoices
        fields=("name","device",)
    def get_device(self,obj):
        serializer=DeviceSerializer(obj.device.all(),many=True)
        return serializer.data
class  DeviceSerializer(serializers.ModelSerializer):
   

    class Meta:
        model=Device
        fields=("name",)

