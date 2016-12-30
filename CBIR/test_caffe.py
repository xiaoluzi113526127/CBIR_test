#coding=utf-8
#获取googlenet模型中输出的pool5/7x7_s1的结果，维数是1024.
#加载必要的库

#设置当前目录
def test_caffe(file_path):
    import numpy as np
    import caffe
    import json
    from PIL import Image
    caffe_root = '/home/st/caffe/'

    # print type(file_path),file_path,'caffe'
    # img = Image.open(file_path)
    # img.show()
    # os.chdir(caffe_root)
    # print type(file_path)
    # caffe.set_mode_cpu() #设置成是cpu运行还是gpu
    im = caffe.io.load_image(file_path)###################图片位置###################
    # print im
    net_file = caffe_root + 'models/bvlc_googlenet/deploy.prototxt'     #测试用的网络配置文件#这个是前向传播时候的网络
    caffe_model = caffe_root + 'models/bvlc_googlenet/bvlc_googlenet.caffemodel'  #训练好的googlenet模型
    mean_file = caffe_root + 'python/caffe/imagenet/ilsvrc_2012_mean.npy' #均值文件得到一个三维数组，3*256*256,mu[0]是B,mu[1] #是G，mu[2]是R
    # print 'sssss'
    net = caffe.Net(net_file,   # defines the structure of the model
                    caffe_model,  # contains the trained weights
                    caffe.TEST)    # use test mode (e.g., don't perform dropout)  ，这些定义都在._caffe中
    # print 'qqqqqqqq'
    # for layer_name, blob in net.blobs.iteritems():  #每层的结果
    #     print layer_name + '\t' + str(blob.data.shape)
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape}) #定义一个实例，字典存储在self.inputs中  #blob是基础的数据结构，是用来保存学习到的参数以及网络传输过程中产生数据的类
    transformer.set_transpose('data', (2, 0, 1))  # move image channels to outermost dimension （2,0,1）存储在self.transpose['data']=order
    transformer.set_mean('data', np.load(mean_file).mean(1).mean(1))    # average over pixels to obtain the mean (BGR) pixel values，计算均值，输出是一个三维向量。
    transformer.set_raw_scale('data', 255) #设置图片规格
    transformer.set_channel_swap('data', (2, 1, 0))    # swap channels from RGB to BGR</span
    net.blobs['data'].data[...] = transformer.preprocess('data', im) #数据预处理# copy the image data into the memory allocated for the net
    out = net.forward()    #前向传播


    imagenet_labels_filename = caffe_root + 'data/ilsvrc12/synsets_china.txt'
    labels = np.loadtxt(imagenet_labels_filename, str, delimiter='\t')  #数据标签文件
    top_k = net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]      # 输出概率最大的前5个预测结果
    list_image_name = []
    for i in np.arange(top_k.size):
        image_n = str(labels[top_k[i]]).split(' ')[1]
        # print image_n
        list_image_name.append(image_n)
    # image_name = labels[top_k[0]]
    list_image_name = json.dumps(list_image_name, encoding="UTF-8", ensure_ascii=False)
    # print list_image_name

    # print net.blobs['pool5/7x7_s1'].data[0].flatten().tolist() #pool5/7x7_s1层的输出结果为1024维
    return net.blobs['pool5/7x7_s1'].data[0].flatten().tolist(), list_image_name #pool5/7x7_s1层的输出结果为1024维
# print test_caffe('/home/st/PycharmProjects/CBIR_test/image/1.jpg')