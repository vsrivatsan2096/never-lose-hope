from keras.callbacks import ModelCheckpoint
from keras.models import Model, Sequential
from keras.layers import Dense, Activation, Dropout, Input, Masking, TimeDistributed, LSTM, Conv1D
from keras.layers import GRU, Bidirectional, BatchNormalization, Reshape
from keras.optimizers import Adam

def model(input_shape):
    x = Input(shape=input_shape)
    
    # CONVULUTIONAL LAYER
    X = Conv1D(196, kernel_size=15, strides=4)(x)
    X = BatchNormalization()(X)
    X = Activation('relu')(X)
    X = Dropout(0.8)(X)
    
    #FIRST GRU LAYER
    X = GRU(units=128, return_sequences=True)(X)
    X = Dropout(0.8)(X)
    X = BatchNormalization()(X)
    
    #SECOND GRU LAYER
    X = GRU(units=128, return_sequences=True)(X)
    X = Dropout(0.8)(X)
    X = BatchNormalization()(X)
    X = Dropout(0.8)(X)
    
    #TIME DISTRIBUTED DENSE LAYER
    X = TimeDistributed(Dense(1, activation="sigmoid"))(X)
    model = Model(inputs=x, outputs=X)
    return model

def main(Tx, n_freq):
    model1 = model((Tx, n_freq))
    opt = Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, decay=0.01)
    model1.compile(loss="binary_crossentropy", optimizer=opt, metrics=["accuracy"])
    return model1