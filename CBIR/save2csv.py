#coding=utf-8
#将1024维的数据保存到CSV中。图片在数据库中的ID和1024维的list列表，图片对应的类label标识，图片数据库中的ID对应的64维特征
import csv
csvfile = file('/home/st/ImageNet/csv_ID_1024_label_64.csv','wb')
writer = csv.writer(csvfile)
writer.writerow(['ID','1024','label','64'])
print 'create_csv_success'
csvfile.close()
def input_datato_csv(data):
    csvfile = file('/home/st/ImageNet/csv_ID_1024_label_64.csv','a')
    writer = csv.writer(csvfile)
    writer.writerows(data)  #写入多行
    csvfile.close()
# data=[ ('小河', '25', '1234567')]
# input_datato_csv(data)
# input_datato_csv(data)
# input_datato_csv(data)





