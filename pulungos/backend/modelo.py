import os

from keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizer_v2
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as K


K.clear_session()
data_entrenamiento = './data/entrenamiento'
data_validacion = './data/validacion'
# parametros
epocas = 20
altura, logitud = 100, 100
batch_size = 32
pasos = 1000
pasos_validacion = 200
filtrosConv1 = 32
filtrosConv2 = 64
tamano_filtro1 = (3, 3)
tamano_filtro2 = (2, 2)
tamano_pool = (2, 2)
clases = 4  # añadir la cantiad de carpetas que hay
lr = 0.0005
# pre procesamiento de imagenes
entrenamiento_dataGen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.3,
    zoom_range=0.3,
    horizontal_flip=True
)
validacion_dataGen = ImageDataGenerator(
    rescale=1./255,
)
imagen_entrenamiento = entrenamiento_dataGen.flow_from_directory(data_entrenamiento,
                                                                 target_size=(altura, logitud), batch_size=batch_size, class_mode='categorical')

images_validacion = validacion_dataGen.flow_from_directory(data_validacion, target_size=(
    altura, logitud), batch_size=batch_size, class_mode='categorical')
# creamos la red neuronal

cnn = Sequential()
cnn.add(Convolution2D(filtrosConv1, tamano_filtro1, padding='same',
        input_shape=(altura, logitud, 3), activation='relu'))
cnn.add(MaxPooling2D(pool_size=tamano_pool))
cnn.add(Convolution2D(filtrosConv2, tamano_filtro2,
        padding='same', activation='relu'))
cnn.add(MaxPooling2D(pool_size=tamano_pool))

cnn.add(Flatten())
cnn.add(Dense(256, activation='relu'))
cnn.add(Dropout(0.5))
cnn.add(Dense(clases, activation='softmax'))

cnn.compile(loss='categorical_crossentropy',
            optimizer=optimizer_v2.adam.Adam(learning_rate=lr), metrics=['accuracy'])
cnn.fit(
    imagen_entrenamiento,
    steps_per_epoch=pasos,
    epochs=epocas,
    validation_data=images_validacion,
    validation_steps=pasos_validacion
)
dir = './modelo/'

if not os.path.exists(dir):
    os.makedirs(dir)
cnn.save('./modelo/modelo.h5')
cnn.save_weights('./modelo/pesos.h5')
