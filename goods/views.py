from django.shortcuts import render, get_object_or_404

from goods.models import Good

def goods_list(request):
    goods = Good.objects.all()
    return render(request, 'goods/goods_list.html',{'goods':goods})


def good_detail(request, pk):
    good = get_object_or_404(Good.objects.all(),pk=pk)
    # Good.objects.get(pk=pk)
    return render(request, 'goods/good_detail.html',{'good':good})