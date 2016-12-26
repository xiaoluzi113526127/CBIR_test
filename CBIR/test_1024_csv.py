# coding: utf-8
#读取存入csv文本中的1024维数据
import csv
import sys
csv.field_size_limit(sys.maxsize)
with open('/home/st/ImageNet/csv_ID_1024_label_64.csv','rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
       print eval(row.get("1024"))





