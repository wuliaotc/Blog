from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from Blog import settings
from app import identity
import os
import datetime
MDEDITOR_CONFIGS = settings.MDEDITOR_CONFIGS['default']

@identity.islogin
def uploadImage(request):
    if request.method=="POST":
        print(vars(request.FILES))
        upload_image = request.FILES.get("editormd-image-file", None)
        media_root = settings.MEDIA_ROOT

        # image none check
        if not upload_image:
            return JsonResponse({
                'success': 0,
                'message': "未获取到要上传的图片",
                'url': ""
            })

        # image format check
        file_name_list = upload_image.name.split('.')
        file_extension = file_name_list.pop(-1)
        file_name = '.'.join(file_name_list)
        if file_extension not in MDEDITOR_CONFIGS['upload_image_formats']:
            return JsonResponse({
                'success': 0,
                'message': "上传图片格式错误，允许上传图片格式为：%s" % ','.join(
                    MDEDITOR_CONFIGS['upload_image_formats']),
                'url': ""
            })

        # image floder check
        file_path = os.path.join(media_root, MDEDITOR_CONFIGS['image_folder'])
        if not os.path.exists(file_path):
            try:
                os.makedirs(file_path)
            except Exception as err:
                return JsonResponse({
                    'success': 0,
                    'message': "上传失败：%s" % str(err),
                    'url': ""
                })

        # save image
        file_full_name = '%s_%s.%s' % (file_name,
                                       '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now()),
                                       file_extension)
        with open(os.path.join(file_path, file_full_name), 'wb+') as file:
            for chunk in upload_image.chunks():
                file.write(chunk)

        return JsonResponse({'success': 1,
                             'message': "上传成功！",
                             'url': os.path.join(settings.MEDIA_URL,
                                                 MDEDITOR_CONFIGS['image_folder'],
                                                 file_full_name)})

# {
#                 success: 0 | 1, //0表示上传失败;1表示上传成功
#                 message : "提示的信息",
#                 url     : "图片地址" //上传成功时才返回
#             }

# {
#                 success: 0 | 1, //0表示上传失败;1表示上传成功
#                 message : "提示的信息",
#                 url     : "图片地址" //上传成功时才返回
#             }