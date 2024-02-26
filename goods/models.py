from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(verbose_name = 'Наименование категории',max_length=255)
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('pk',)

    def __str__(self):
        return self.title
    

class Good(models.Model):
    COLORS_CHOICES = (
        ('red','Красное'),
        ('white','Белое'),
    )

    image = models.ImageField(verbose_name='Изображение', null=True, blank=True)
    category = models.ForeignKey(Category,verbose_name = 'Категория', null = True, blank = True, on_delete = models.CASCADE, related_name = 'goods')
    color = models.CharField(verbose_name = 'Цвет', choices = COLORS_CHOICES, max_length = 255, default = 'red')
    title = models.CharField(max_length = 255, verbose_name = 'Заголовок')
    price = models.IntegerField(default = 0, verbose_name = 'Цена')
    created_at = models.DateTimeField(verbose_name = 'Дата создания', default = timezone.now)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    
    def __str__(self) -> str:
        return f'{self.pk} - {self.title}'
# Create your models here.
