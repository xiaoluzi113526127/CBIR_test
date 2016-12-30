#coding=utf-8
import datetime
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
from django.conf import settings
from PIL import Image
import test_image
# Create your views here.
def sayHello(request):
    s = 'Hello World!'
    current_time = datetime.datetime.now()
    html = '<html><head></head><body><h1> %s </h1><p> %s </p></body></html>' % (s, current_time)
    return HttpResponse(html)


def showInformation(request):
     if request.method == "POST":
        image = request.FILES.get('file')

        path = default_storage.save(image.name, ContentFile(image.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        # path_1 = '../'+tmp_file
        print type(path), path
        print type(tmp_file), tmp_file
        # print type('../image/1_GBQpMA2.jpg'), '../image/1_GBQpMA2.jpg'
        # img = Image.open(tmp_file)
        # img.show()

        # test_image.test_cbir('../image/1_GBQpMA2.jpg', 50, 5)
        # test_image.test_cbir(tmp_file, 50, 5)
        image_path, list_name_image = test_image.test_cbir(tmp_file, 50, 5)

        print image_path
        print list_name_image
        # print type(image), image.name, image.size
        # infor = '/home/st/ImageNet/ILSVRC2012/ILSVRC2012/ILSVRC2012_img_train/n01440764/n01440764_37.JPEG'
        infor1 = '../static/images/'+image_path[0]
        infor2 = '../static/images/'+image_path[1]
        infor3 = '../static/images/'+image_path[2]
        infor4 = '../static/images/'+image_path[3]
        infor5 = '../static/images/'+image_path[4]
        image_name = list_name_image
     else:
        image_name = ''
        infor1 = ''
        infor2 = ''
        infor3 = ''
        infor4 = ''
        infor5 = ''
     # print 'sss'
     return render_to_response('../templates/information.html', {'image_name': image_name, 'image1': infor1, 'image2': infor2, 'image3': infor3, 'image4': infor4, 'image5': infor5})

# test_image.test_cbir('/home/st/PycharmProjects/CBIR_test/image/1_3X5FVdY.jpg', 50, 5)
# test_image.test_cbir('../image/1.jpg', 50, 5)
# test_image.test_cbir('/home/st/ImageNet/ILSVRC2012/ILSVRC2012/ILSVRC2012_img_train/n01440764/n01440764_37.JPEG', 50, 5)