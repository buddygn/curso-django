from django.db import models
from django.urls import reverse
from django_extensions.db.fields import RandomCharField
from ordered_model.models import OrderedModel


class Modulo(OrderedModel):
    titulo = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)
    publico = models.TextField()
    descricao = models.TextField()

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('modulos:detalhe', kwargs={'slug': self.slug})


class Aula(OrderedModel):
    titulo = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)
    modulo = models.ForeignKey(Modulo, on_delete=models.PROTECT)
    vimeo_id = models.CharField(max_length=32)
    teste = RandomCharField(length=12, unique=True)

    order_with_respect_to = 'modulo'

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('modulos:aula', kwargs={'slug': self.slug})
