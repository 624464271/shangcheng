from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from meiduo.libs.captcha.captcha import captcha
from django_redis import get_redis_connection
from . import constants
# from . import constants

# url('^image_codes/(?P<image_code_id>[\w-]+)/$', views.ImageCodeView.as_view()),
class ImageCodeView(APIView):
    """
    图片验证码
    """
    pass
    #test


class ImageCodeView(APIView):
    """
    图片验证码
    """

    def get(self, request, image_code_id):
        """
        获取图片验证码
        """
        # 生成验证码图片
        text, image = captcha.generate_captcha()
        captcha


        redis_conn = get_redis_connection("verify")
        redis_conn.setex("img_%s" % image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES, text)
        # redis_conn.setex("img_%s" % image_code_id, 300,text)

        # 固定返回验证码图片数据，不需要REST framework框架的Response帮助我们决定返回响应数据的格式
        # 所以此处直接使用Django原生的HttpResponse即可
        return HttpResponse(image, content_type="images/jpg")

class SMSCodeView():

    """
    短信验证码
    传入参数：
        mobile, image_code_id, text
    """
    def get(self,request):

        pass
        # 获取前端数据
        # 数据验证
        # 生成短信验证码
        # 保存短信验证码
        # 发送短信
        # 结果返回
