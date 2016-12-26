# coding: utf-8
import random
import linecache
import csv
#############得到打乱顺序的数据+标签/home/st/ImageNet/data_1024.csv##############
row_len = 0
####设置train和test的比例(1/10) #####
rate = 10

fobj = open('/home/st/ImageNet/csv_ID_1024_label_64.csv','rb')
for i in fobj:
    row_len +=1    #得到文本的行数
fobj.close()

count = 0
index = [i+1 for i in range(row_len)]
random.shuffle(index) #得到随机打乱的标签
input_train = open('/home/st/ImageNet/data_1024_train.csv','wb') #新保存的训练数据位置
writer_trian = csv.writer(input_train)
writer_trian.writerow(['ID','1024','label','64'])

input_test = open('/home/st/ImageNet/data_1024_test.csv','wb') #新保存的测试数据位置
writer_test = csv.writer(input_test)
writer_test.writerow(['ID','1024','label','64'])


for i in range(row_len):
    count +=1
    if index[i]!=1 and count<(row_len-row_len//rate):
        data = linecache.getline(r'/home/st/ImageNet/csv_ID_1024_label_64.csv',index[i])  #注意路径
        input_train.write(data)
    elif index[i]!=1 and count>=(row_len-row_len//rate):
        data = linecache.getline(r'/home/st/ImageNet/csv_ID_1024_label_64.csv',index[i])  #注意路径
        input_test.write(data)
input_train.close()
input_test.close()

#
#
#
# print 121//10