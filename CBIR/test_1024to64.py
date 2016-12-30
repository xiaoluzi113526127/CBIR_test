#coding=utf-8
#######训练1024到64维的模型#########
import h5py
from keras.layers.core import Dense,Dropout,Activation, Flatten
from keras.models import Sequential
from sklearn.externals import joblib
import numpy as np
from keras.utils import np_utils
from  keras.callbacks import ModelCheckpoint,Callback
import sys
sys.setrecursionlimit(100000)   #手工设置递归调用深度
import csv
sys.setrecursionlimit(100000)   #手工设置递归调用深度
csv.field_size_limit(sys.maxsize)

class LossHistory(Callback):
    def on_train_begin(self, logs={}):
        self.losses = []
    def on_batch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))

train_data_len = 0
train_data = open('/home/st/ImageNet/data_1024_train.csv','rb')
for i in train_data:
    train_data_len +=1    #得到文本的行数
train_data.close()

test_data_len = 0
test_data = open('/home/st/ImageNet/data_1024_test.csv','rb')
for i in test_data:
    test_data_len +=1    #得到文本的行数
test_data.close()


n = 25  ###设置类别数###

#####训练项数据######
def generate_batch_data_random_train(batch_size):
    loopcount = (train_data_len-1)//batch_size
    while(True):
        for i in range(0,loopcount+1,1):
            with open('/home/st/ImageNet/data_1024_train.csv','rb') as csvfile:
                reader = csv.DictReader(csvfile)
                data_sum = []
                label_sum = []
                for idx, row in enumerate(reader):
                    if idx >= i*batch_size and idx < (i+1)*batch_size:
                        data = eval(row.get("1024"))
                        data_sum.append(data)
                        label = eval(row.get("label"))-1    #注意
                        label_sum.append(label)
                data_sum = np.array(data_sum)
                label_sum = np_utils.to_categorical(label_sum, n)   #注意n
                yield data_sum, label_sum


#####测试项数据######
def generate_batch_data_random_val(batch_size):
    loopcount = (test_data_len-1)//batch_size
    while(True):
        for i in range(0,loopcount+1,1):
            with open('/home/st/ImageNet/data_1024_test.csv','rb') as csvfile:
                reader = csv.DictReader(csvfile)
                data_sum = []
                label_sum = []
                for idx, row in enumerate(reader):
                    if idx >= i*batch_size and idx < (i+1)*batch_size:
                        data = eval(row.get("1024"))
                        data_sum.append(data)
                        label = eval(row.get("label"))-1    #注意
                        label_sum.append(label)
                data_sum = np.array(data_sum)
                label_sum = np_utils.to_categorical(label_sum, n)#注意n
                yield data_sum, label_sum



model=Sequential()
model.add(Dense(64,activation='sigmoid',input_dim=1024))
model.add(Dense(n))  #注意修改n
model.add(Activation('softmax'))
model.compile(loss='categorical_crossentropy',
              optimizer='SGD',
              metrics=['accuracy'])
checkpointer =ModelCheckpoint(filepath='../model_1024to64_weights.h5', verbose=1, save_best_only=True)
history = LossHistory()
model.fit_generator(generate_batch_data_random_train(80),samples_per_epoch=train_data_len-1,validation_data=generate_batch_data_random_val(50),nb_val_samples=test_data_len-1,nb_epoch=10,verbose=1,callbacks=[checkpointer,history])
model_json = model.to_json()  #等价于 json_string = model.get_config()
with open("../model_1024to64.json", "w") as json_file:
    json_file.write(model_json)
# model.save_weights('model_1024to64_weights.h5')#保存模型和权重
