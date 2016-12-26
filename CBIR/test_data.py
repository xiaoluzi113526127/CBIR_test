#coding:utf-8
#######打乱顺序后的数据中取出规定size的数据作为训练#########
import numpy as np
import csv
import sys

from keras.utils import np_utils
csv.field_size_limit(sys.maxsize)

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

n = 25 #注意修改类别数
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
                label_sum = np_utils.to_categorical(label_sum, n)#注意修改类别标签数
                yield data_sum,label_sum

# generate_batch_data_random_train(1000)

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
                label_sum = np_utils.to_categorical(label_sum, n)#注意修改类别标签数
                print data_sum,label_sum

# generate_batch_data_random_val(1000)


######获取指定位置的数据########
# with open('/home/st/ImageNet/data_1024.csv','rb') as csvfile:
#     reader = csv.DictReader(csvfile)
#     data_sum = []
#     label_sum = []
#     for idx, row in enumerate(reader):
#         if idx >= 20 and idx <= 200:
#             data = eval(row.get("1024"))
#             label = eval(row.get("label"))-1
#             data_sum.append(data)
#             label_sum.append(label)
#     data_sum = np.array(data_sum)
#     label_sum = np_utils.to_categorical(label_sum, 2)#注意修改
#     print data_sum
#     print label_sum


