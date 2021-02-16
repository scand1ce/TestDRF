from django.db import models


class Discr(models.Model):
    description = models.TextField(max_length=1000, blank=True, verbose_name='Характеристики предмета из коробки')

    def __str__(self):
        return self.description


class Item(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название предмета из коробки')
    quantity = models.PositiveIntegerField('Количество товара', default=1)
    description = models.ManyToManyField(Discr,
                                         verbose_name="характеристики",
                                         related_name="descriptions"
                                         )

    def __str__(self):
        return self.title


class Box(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название коробки')
    item = models.ManyToManyField(Item,
                                  verbose_name="предметы",
                                  related_name="items"
                                  )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания коробки')

    def __str__(self):
        data_ = "Name: %s; || Date: %s" % (self.title, self.created_at)
        return data_

    class Meta:
        verbose_name = 'Коробка'
        verbose_name_plural = 'Коробки'
        ordering = ['-created_at', '-title']
