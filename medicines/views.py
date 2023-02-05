#from django.shortcuts import render
from .models import Medicines
#from django.http import JsonResponse
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MedicineSerializer, MedicineCrearSerializer

@api_view(['GET', 'POST'])
def index (request):

    if request.method == 'GET':
        medicines = Medicines.objects.all()
        serializados = MedicineSerializer(medicines, many=True)
        return Response(serializados.data)
    else:
        #medicines = Medicines.objects.create
        serializados = MedicineSerializer(request.data)
        if serializados.is_valid():
            serializados.create(
            name = request.data['name'],
            price= request.data['price'],
            laboratory_id =request.data['laboratory_id']
            )
        return Response(serializados.data)

"""  
    #return 'hola mundo'
    medicines = Medicines.objects.all()

    result = [
    ]

    for m in medicines:

        med = { 
            'id': m.id,
            'name':m.name,
            'price':m.price

        }
    result.append(med)

    return JsonResponse(
       {
        'data': result,
        
        'code': 200,
        
        'message': 'ok'
       }
    )
"""

@api_view(['GET', 'PUT', 'DELETE'])
def detail (request, pk):
    medicines = Medicines.objects.filter(id=pk).first()
    
    if request.method =='GET':
        

        pass
        
        
    
    if request.method =='PUT':
       
       serializados = MedicineCrearSerializer(data=request.data)

       if serializados.is_valid():
           
        medicines.name = request.data['name']
        medicines.price = request.data['price']

        medicines.save()
           
    if request.method =='DELETE':

        medicines.delete()
    
    serializados = MedicineSerializer(medicines)

    return Response(serializados.data) 
        

    pass