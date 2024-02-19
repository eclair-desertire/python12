from django.shortcuts import render, get_object_or_404, redirect

from goods.models import Good
from goods.forms import GoodForm

def goods_list(request):
    goods = Good.objects.all()
    return render(request, 'goods/goods_list.html',{'goods':goods})


def good_detail(request, pk):
    good = get_object_or_404(Good.objects.all(),pk=pk)
    # Good.objects.get(pk=pk)
    return render(request, 'goods/good_detail.html',{'good':good})


def good_new(request):
    if request.method == "POST":
        form = GoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            good = form.instance
            return redirect('good_detail', pk=good.pk)
    else:
        form = GoodForm()
    return render(request, 'goods/good_new.html',{'form':form})


def good_edit(request, pk):
    good = get_object_or_404(Good.objects.all(),pk=pk)

    if request.method == "POST":
        form = GoodForm(request.POST, request.FILES, instance=good)
        if form.is_valid():
            form.save()
            good = form.instance
            return redirect('good_detail', pk=good.pk)
    else:
        form = GoodForm(instance=good)
    return render(request, 'goods/good_edit.html',{'form':form, 'good':good})