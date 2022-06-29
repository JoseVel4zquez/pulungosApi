# from backend.models import preguntas
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from rest_framework.response import Response
# from backend.serializers import preguntasSerializer
# from django.contrib.auth.hashers import make_password
# from rest_framework import status
# from tensorflow.keras.utils import img_to_array, load_img

# from keras.models import load_model
# import numpy as np

# longitud, altura = 100, 100
# # modelo = 'C:/Users/hp/Desktop/JavaScript/api/pulungosApi/pulungos/backend/modelo/modelo.h5'
# # pesos = 'C:/Users/hp/Desktop/JavaScript/api/pulungosApi/pulungos/backend/modelo/pesos.h5'
# cnn = load_model(modelo)
# cnn.load_weights(pesos)


# @api_view(['POST'])
# def predict(request):
#     files = request.FILES.get('image')
#     x = load_img(files, target_size=(longitud, altura))
#     x = img_to_array(x)
#     x = np.expand_dims(x, axis=0)
#     arreglo = cnn.predict(x)
#     resultado = arreglo[0]
#     respuesta = np.argmax(resultado)
#     if respuesta == 0:
#         return Response('Diagnostico: amigdalitis')
#     elif respuesta == 1:
#         return Response('Diagnostico: dientes con caries')
#     elif respuesta == 2:
#         return Response('Diagnostico: Dientes saludables')
#     elif respuesta == 3:
#         return Response('Diagnostico: Encias con gingicitis')
