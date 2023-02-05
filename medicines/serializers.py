from rest_framework import serializers
from .models import Medicines
from laboratories.models import laboratory

class LaboratorySerializer (serializers.ModelSerializer):
     class Meta:
         model = laboratory
         fields =['id', 'name']

    


class MedicineSerializer (serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    price = serializers.IntegerField()
    laboratory_id = serializers.CharField()

    laboratory = LaboratorySerializer(read_only=True)
    


    def create  (self,name, price, lab):
        return Medicines.objects.create(
    
           name= name,
           price=price,
           laboratory_id = lab

          
        )
    


class MedicineCrearSerializer (serializers.Serializer):
    
    name = serializers.CharField()
    price = serializers.IntegerField()
  