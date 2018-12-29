#!/usr/bin/python
# -*- coding: UTF-8 -*-  
# RaspberryGPIO - fileUpload.py
# 2018/12/20 23:01
# Author:Kencin <myzincx@gmail.com>

import QiNiuOSS.config as config
from qiniu import Auth, put_file, etag


class FileUpload(object):
    # 上传到七牛后保存的文件名
    key = ''
    # 要上传文件的本地路径
    local_file = ''
    file_url = config.file_url

    def __init__(self, key, local_file):
        self.key = key
        self.local_file = local_file

    def upload(self):
        q = Auth(config.access_key, config.secret_key)
        token = q.upload_token(config.bucket_name, self.key, 3600)
        ret, info = put_file(token, self.key, self.local_file)
        print(info)
