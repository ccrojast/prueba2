# Create your views here.
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
import tutorials.models as models
import tutorials.serializers as serializers
from rest_framework.decorators import api_view


#@api_view(['GET', 'POST', 'DELETE'])
#def tutorial_list(request):
#    if request.method == 'GET':
#        tutorials = models.Tutorial.objects.all()
#        
#        title = request.GET.get('title', None)
#        if title is not None:
#            tutorials = tutorials.filter(title__icontains=title)
#        
#        tutorials_serializer = serializers.TutorialSerializer(tutorials, many=True)
#        return JsonResponse(tutorials_serializer.data, safe=False)
#        # 'safe=False' for objects serialization
# 
#    elif request.method == 'POST':
#        tutorial_data = JSONParser().parse(request)
#        tutorial_serializer = serializers.TutorialSerializer(data=tutorial_data)
#        if tutorial_serializer.is_valid():
#            tutorial_serializer.save()
#            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
#        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#    elif request.method == 'DELETE':
#       count = serializers.Tutorial.objects.all().delete()
#        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
#@api_view(['GET', 'PUT', 'DELETE'])
#def tutorial_detail(request, pk):
#    try: 
#        tutorial = serializers.Tutorial.objects.get(pk=pk) 
#    except serializers.Tutorial.DoesNotExist: 
#        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
# 
#    if request.method == 'GET': 
#        tutorial_serializer = serializers.TutorialSerializer(tutorial) 
#        return JsonResponse(tutorial_serializer.data) 
 
 #   elif request.method == 'PUT': 
 #       tutorial_data = JSONParser().parse(request) 
 #       tutorial_serializer = serializers.TutorialSerializer(tutorial, data=tutorial_data) 
 #       if tutorial_serializer.is_valid(): 
 #           tutorial_serializer.save() 
 #           return JsonResponse(tutorial_serializer.data) 
 #       return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 #
 #   elif request.method == 'DELETE': 
 #       tutorial.delete() 
 #       return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
#@api_view(['GET'])
#def tutorial_list_published(request):
#    tutorials = serializers.Tutorial.objects.filter(published=True)
#        
#    if request.method == 'GET': 
#        tutorials_serializer = serializers.TutorialSerializer(tutorials, many=True)
#        return JsonResponse(tutorials_serializer.data, safe=False)

#######################################
#######################################

@api_view(['GET', 'POST'])
def comentarios_producto(request):
    if request.method == 'GET':
        comentarios1 = models.comentarios.objects.all()
        id_comentarios = request.GET.get('id', None)
        if id_comentarios is not None:
            comentarios1 = comentarios1.filter(id=id_comentarios)
        
        comentario_serializer = serializers.comentarioSerializer(comentarios1, many=True)
        return JsonResponse(comentario_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        comentarios_data = JSONParser().parse(request)
        print(comentarios_data)
        comentarios_serializer = serializers.comentarioSerializer(data=comentarios_data)
        print(comentarios_serializer.is_valid())
        if comentarios_serializer.is_valid():
            comentarios_serializer.save()
            print(comentarios_serializer.data)
            return JsonResponse(comentarios_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(serializers.comentarios_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def preguntas_producto(request):
    if request.method == 'GET':
        preguntas1 = models.pregunta.objects.all()
        id_preguntas = request.GET.get('id', None)
        if id_preguntas is not None:
            preguntas1 = preguntas1.filter(id=id_preguntas)
        
        preguntas_serializer = serializers.preguntaSerializer(preguntas1, many=True)
        return JsonResponse(preguntas_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        preguntas_data = JSONParser().parse(request)
        preguntas_serializer = serializers.preguntaSerializer(data=preguntas_data)
        if preguntas_serializer.is_valid():
            preguntas_serializer.save()
            return JsonResponse(preguntas_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(preguntas_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def calificaciones_producto(request):
    if request.method == 'GET':
        calificaciones1 = models.calificaciones.objects.all()
        id_calificaciones = request.GET.get('id', None)
        if id_calificaciones is not None:
            calificaciones1 = calificaciones1.filter(id=id_calificaciones)
        
        calificaciones_serializer = serializers.calificacionSerializer(calificaciones1, many=True)
        return JsonResponse(calificaciones_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        calificaciones_data = JSONParser().parse(request)
        calificaciones_serializer = serializers.calificacionSerializer(data=calificaciones_data)
        if calificaciones_serializer.is_valid():
            calificaciones_serializer.save()
            return JsonResponse(calificaciones_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(calificaciones_serializer.errors, status=status.HTTP_400_BAD_REQUEST)