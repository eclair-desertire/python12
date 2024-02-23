from django.urls import path, include

from api.views import GoodList, GoodDetail

urlpatterns = [
    path('goods/', GoodList.as_view()),
    path('good/<int:pk>/', GoodDetail.as_view())
]
