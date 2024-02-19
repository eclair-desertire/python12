from django.urls import path, include

from goods.views import goods_list, good_detail, good_new, good_edit

urlpatterns = [
    path('',goods_list, name='goods_list'),
    path('<int:pk>/detail/',good_detail, name='good_detail'),
    path('<int:pk>/edit/',good_edit ,name = 'good_edit'),
    path('new/',good_new,name='good_new'),
]
