#coding=utf-8
from keras.models import model_from_json
import tensorflow
import numpy as np
from keras import backend as K
import csv
import sys
csv.field_size_limit(sys.maxsize)
import os, django
os.environ['DJANGO_SETTINGS_MODULE'] = 'CBIR_test.settings'
django.setup()
from CBIR.models import CBIRS_64_Feature


######输出中间层的结果#####
def data_1024t064(data):
    #加载模型数据和weights
    json_file = open('model_1024to64.json', 'rb')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("model_1024to64_weights.h5")
    # loaded_model.predict('data').
    # print loaded_model.summary()
    # print loaded_model.get_config()
    f = K.function([loaded_model.layers[0].input, K.learning_phase()], [loaded_model.layers[0].output])
    output = f([data, 0])
    # output = loaded_model.predict(data, batch_size=1, verbose=0)
    return output[0][0]  #返回64维的数据array


csvfile = file('/home/st/csv_ID_64.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(['ID', '64'])
print 'create_csv_success'
csvfile.close()
#####保存######
with file('/home/st/ImageNet/csv_ID_64.csv', 'a') as csvfile_64:
    with open('/home/st/ImageNet/csv_ID_1024_label_64.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile)  #能返回一个生成器，但是返回的每一个单元格都放在一个字典的值内，而这个字典的键则是这个单元格的标题（即列头）
        for idx, row in enumerate(reader):
            # print type(row.get('1024'))
            # print row.get('1024')
            list = []
            list.append(eval(row.get("1024")))
            s = np.array(list)
            # print type(s), s
            data = data_1024t064(s)
            # print data
            data[data < 0.5] = 0
            data[data >= 0.5] = 1
            # print data
            data = map(int, data)
            data = map(str, data)
            # print type(data), data
            data = ''.join(data)
            writer = csv.writer(csvfile_64)
            writer.writerows([(row.get('ID'), [data])])  #写入多行
            #####哈希码保存到数据库######
            feature_64 = CBIRS_64_Feature()
            feature_64.id = row.get('ID')
            feature_64.value = [data]
            feature_64.tag = [data[0:5]]
            feature_64.save()

