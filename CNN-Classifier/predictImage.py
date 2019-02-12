#!/usr/bin/python
#coding:utf-8

from django.http import HttpResponse
from predict import *
import json
import time
import os
import re
import base64
from cStringIO import StringIO

from PIL import Image

def recognition(request):
    if request.method == 'POST':
        base64Str = request.POST['image']
        nowStr = time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime(time.time()))
        imagePath = os.path.join('static', 'pic', nowStr + r".jpeg")
        base64_to_image(base64Str, imagePath)
        imageType = predictImage(imagePath)
        os.remove(imagePath)
    if imageType == 0:
        data = {
            'resultsCode': str(imageType),
        }
        resp = {
            'status': '0',
            'msg': '成功',
            'data': data,
        }
    return HttpResponse(json.dumps(resp, {'ensure_ascii':False}), content_type="application/json")

def base64_to_image(base64_str, image_path=None):
    base64_data = re.sub('^data:image/.+;base64,', '', base64_str)
    binary_data = base64.b64decode(base64_data)
    img_data = StringIO(binary_data)
    img = Image.open(img_data)
    if image_path:
        img.save(image_path)
    return img
