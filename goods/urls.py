from django.urls import path, include

from goods.views import goods_list, good_detail

urlpatterns = [
    path('',goods_list, name='goods_list'),
    path('<str:title>/detail/',good_detail, name='good_detail')
]
