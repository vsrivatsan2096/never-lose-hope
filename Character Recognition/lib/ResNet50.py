from keras import Input, Model
from keras.layers import ZeroPadding2D, Conv2D, BatchNormalization, Activation, AveragePooling2D, Flatten, Dense
from resnet_blocks import convolutional, identity


class ResNet50:
    def __init__(self, input_shape, classes):
        self.input = Input(input_shape)
        self.classes = classes

    def get_model(self):
        X = ZeroPadding2D((3, 3))(self.input)
        X = Conv2D(64, (7, 7), strides=(2, 2), name='conv1', kernel_initializer='glorot_uniform')(X)
        Z = BatchNormalization(axis=3, name="bn_conv1")(X)
        A = Activation('relu')(Z)

        X = convolutional(inputs=A, middle_shape=3, filters=[64, 64, 256], stage=2, block='a', s=1)
        X = identity(inputs=X, middle_shape=3, filters=[64, 64, 256], stage=2, block='b')
        X = identity(inputs=X, middle_shape=3, filters=[64, 64, 256], stage=2, block='c')

        X = convolutional(inputs=X, middle_shape=3, filters=[128, 128, 512], stage=3, block='a', s=2)
        X = identity(inputs=X, middle_shape=3, filters=[128, 128, 512], stage=3, block='b')
        X = identity(inputs=X, middle_shape=3, filters=[128, 128, 512], stage=3, block='c')
        X = identity(inputs=X, middle_shape=3, filters=[128, 128, 512], stage=3, block='d')

        X = convolutional(inputs=X, middle_shape=3, filters=[256, 256, 1024], stage=4, block='a', s=2)
        X = identity(inputs=X, middle_shape=3, filters=[256, 256, 1024], stage=4, block='b')
        X = identity(inputs=X, middle_shape=3, filters=[256, 256, 1024], stage=4, block='c')
        X = identity(inputs=X, middle_shape=3, filters=[256, 256, 1024], stage=4, block='d')
        X = identity(inputs=X, middle_shape=3, filters=[256, 256, 1024], stage=4, block='e')
        X = identity(inputs=X, middle_shape=3, filters=[256, 256, 1024], stage=4, block='f')

        X = convolutional(inputs=X, middle_shape=3, filters=[512, 512, 2048], stage=5, block='a', s=2)
        X = identity(inputs=X, middle_shape=3, filters=[512, 512, 2048], stage=5, block='b')
        X = identity(inputs=X, middle_shape=3, filters=[512, 512, 2048], stage=5, block='c')

        X = AveragePooling2D()(X)

        X = Flatten()(X)

        A = Dense(self.classes, activation='softmax', name="FullyConnected", kernel_initializer="glorot_uniform")(X)

        model = Model(inputs=self.input, outputs=A, name="ResNet50")

        return model