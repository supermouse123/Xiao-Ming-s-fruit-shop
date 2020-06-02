#使用celery发送邮件
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fruitshop.settings")
django.setup()

from django.core.mail import send_mail
from django.conf import settings
from goods.models import GoodsType, IndexGoodsBanner, IndexPromotionBanner, IndexTypeGoodsBanner
from django.template import loader, RequestContext
from django_redis import get_redis_connection
from celery import Celery
import time



#创建一个Celery类的实例对象
app = Celery('celery_tasks.tasks', broker='redis://119.3.189.181:6379/9')

#定义任务函数
@app.task
def send_register_active_email(to_email, username, token):
    """发送激活邮件"""
    subject = '水果商店欢迎信息'
    message = ''
    sender = settings.EMAIL_FROM
    receiver = [to_email]
    html_message = '<h1>%s,欢迎成为水果商店会员</h1>请点击下面链接激活用户</br><a href="http://127.0.0.1:8000/user/active/%s">http://127.0.0.1:8000/user/active/%s</a>' % (
    username, token, token)
    send_mail(subject, message, sender, receiver, html_message=html_message)
    time.sleep(5)


@app.task
def generate_static_index_html():
    # 获取商品种类信息
    types = GoodsType.objects.all()

    # 获取首页轮播信息
    goods_banners = IndexGoodsBanner.objects.all().order_by('index')

    # 获取首页促销活动信息
    promotion_banners = IndexPromotionBanner.objects.all().order_by('index')

    # 获取首页分类商品展示信息
    for type in types:
        # 获取type种类首页分类商品图片信息
        image_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=1).order_by('index')
        # 获取type种类首页分类商品文字信息
        title_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=0).order_by('index')

        # 动态type增加属性
        type.image_banners = image_banners
        type.title_banners = title_banners

    context = {
            'types': types,
            'goods_banners': goods_banners,
            'promotion_banners': promotion_banners}
    temp = loader.get_template('static_index.html')
    static_index_html = temp.render(context)
    print(static_index_html)

    save_path = os.path.join(settings.BASE_DIR, 'static/index.html')
    print(save_path)
    with open(save_path, "w", encoding='utf-8') as f:
        f.write(static_index_html)

