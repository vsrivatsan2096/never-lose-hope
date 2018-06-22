import numpy as np
import tensorflow as tf
import keras.backend as backend
from keras.layers import Add, Activation, BatchNormalization, Conv2D


def convolutional(inputs, middle_shape, filters, stage, block, s=2):
    conv_name = "residualconv" + str(stage) + block + "_branch"
    batch_name = "batch_normconv" + str(stage) + block + "_branch"

    filter1, filter2, filter3 = filters

    shortcut_inputs = inputs

    X = Conv2D(filters=filter1, kernel_size=(1, 1), strides=(s, s), padding='valid',
               name=conv_name + '2a', kernel_initializer='glorot_uniform')(inputs)
    Z = BatchNormalization(axis=3, name=batch_name + '2a')(X)
    A = Activation('relu')(Z)

    X = Conv2D(filters=filter2, kernel_size=(middle_shape, middle_shape), strides=(1, 1), padding='same',
               name=conv_name + '2b', kernel_initializer='glorot_uniform')(A)
    Z = BatchNormalization(axis=3, name=batch_name + '2b')(X)
    A = Activation('relu')(Z)

    X = Conv2D(filters=filter3, kernel_size=(1, 1), strides=(1, 1), padding='valid',
               name=conv_name + '2c', kernel_initializer='glorot_uniform')(A)
    Z = BatchNormalization(axis=3, name=batch_name + '2c')(X)

    shortcut_X = Conv2D(filters=filter3, kernel_size=(1, 1), strides=(s, s), padding='valid',
                        name=conv_name + '1', kernel_initializer='glorot_uniform')(shortcut_inputs)
    shortcut_Z = BatchNormalization(axis=3, name=batch_name + '1')(shortcut_X)

    Z = Add()([Z, shortcut_Z])
    A = Activation('relu')(Z)

    return A


def identity(inputs, middle_shape, filters, stage, block):
    conv_name = "residualid" + str(stage) + block + "_branch"
    batch_name = "batch_normid" + str(stage) + block + "_branch"

    filter1, filter2, filter3 = filters

    residue_inputs = inputs

    X = Conv2D(filters=filter1, kernel_size=(1, 1), strides=(1, 1), padding='valid',
               name=conv_name + '2a', kernel_initializer='glorot_uniform')(inputs)
    Z = BatchNormalization(axis=3, name=batch_name + '2a')(X)
    A = Activation('relu')(Z)

    X = Conv2D(filters=filter2, kernel_size=(middle_shape, middle_shape),
               strides=(1, 1), padding='same', name=conv_name + '2b', kernel_initializer='glorot_uniform')(A)
    Z = BatchNormalization(axis=3, name=batch_name + '2b')(X)
    A = Activation('relu')(Z)

    X = Conv2D(filters=filter3, kernel_size=(1, 1), strides=(1, 1), padding='valid',
               name=conv_name + '2c', kernel_initializer='glorot_uniform')(A)
    Z = BatchNormalization(axis=3, name=batch_name + '2c')(X)

    Z = Add()([Z, residue_inputs])
    A = Activation('relu')(Z)

    return A


def test_identity_block():
    with tf.Session() as test_identity:
        np.random.seed(1)
        A_prev = tf.placeholder("float", [3, 4, 4, 6])
        X = np.random.randn(3, 4, 4, 6)
        A = identity(A_prev, middle_shape=2, filters=[2, 4, 6], stage=1, block='a')
        test_identity.run(tf.global_variables_initializer())
        output = test_identity.run([A], feed_dict={A_prev: X, backend.learning_phase(): 0})
        print("Output = " + str(output[0][1][1][0]))


def test_convolutional_block():
    with tf.Session() as test_identity:
        np.random.seed(1)
        A_prev = tf.placeholder("float", [3, 4, 4, 6])
        X = np.random.randn(3, 4, 4, 6)
        A = convolutional(A_prev, middle_shape=2, filters=[2, 4, 6], stage=1, block='a')
        test_identity.run(tf.global_variables_initializer())
        output = test_identity.run([A], feed_dict={A_prev: X, backend.learning_phase(): 0})
        print("Output = " + str(output[0][1][1][0]))


def main():
    test_identity_block()
    test_convolutional_block()


if __name__ == "__main__":
    main()
