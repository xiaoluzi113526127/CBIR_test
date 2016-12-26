#coding=utf-8
#加载必要的库
import os,django
os.environ["GLOG_minloglevel"] = "2"  #表示不输出日志信息
import test_caffe
import save2csv
caffe_root = '/home/st/caffe/'
os.environ['DJANGO_SETTINGS_MODULE'] = 'CBIR_test.settings'
django.setup()
from CBIR.models import CBIRS_IMAGE,CBIRS_1024_Feature
count = 0
#获取ImageNet文件下图片的绝对路径
dir="/home/st/ImageNet/ILSVRC2012/ILSVRC2012/ILSVRC2012_img_train"
#加载所有图片到数据库并基于googlenet模型计算1024维的输出结果
for d in os.listdir(dir):
    roots = os.path.join(dir, d)  #图片所在类别的绝对路径
    count +=1
    for files in os.listdir(roots):
                # print d,os.path.join(roots,files) #os.path.join(roots,files)是图片的绝对路径...d是该图片所在的类别
                images = CBIRS_IMAGE()
                images.class_name = d
                images.local = os.path.join(roots, files)
                images.save()  #保存到数据库
                get_id = images.id
                label = count
                # print get_id,images.local,label
                get_1024 = test_caffe.test_caffe(images.local) #1024维的数据
                ###保存1024维数据到数据库####
                feature_1024 = CBIRS_1024_Feature()
                feature_1024.id = get_id
                feature_1024.value = get_1024
                feature_1024.save()
                # print get_1024
                data = [(get_id, get_1024, label)]
                # print data
                save2csv.input_datato_csv(data)
    print count




