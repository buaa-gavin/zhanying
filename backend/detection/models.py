import os

from django.db import models
from django.utils import timezone

from algorithm.efficientnet.effb6 import effb6_apply
from algorithm.unet.UnetSemantic import unet_semantic


class Person(models.Model):
    UNKNOWN = "unknown"
    MALE = "m"
    FEMALE = "f"
    GENDER_IN_CHOICES = [
        (UNKNOWN, "未知性别"),
        (MALE, "男"),
        (FEMALE, "女")
    ]
    name = models.CharField(verbose_name="姓名", max_length=255, null=False, default="未知病人")
    birth = models.DateField(verbose_name="出生日期", auto_now_add=True)
    sex = models.CharField(verbose_name="性别", max_length=10, choices=GENDER_IN_CHOICES, default=UNKNOWN)
    updated = models.DateTimeField(verbose_name="最近检测时间", auto_now=True, null=True)

    class Meta:
        ordering = ('-updated',)


class Diagnose(models.Model):
    content = models.ImageField(upload_to='images/%Y%m%d')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, blank=True)
    semantic = models.ImageField(max_length=255, blank=True)
    # 多对一关系，多个诊断结果对应多个Person,反向查询时，是在p = Person.objects.get(id=1);p.diagnose_set 获取所有信息
    person = models.ForeignKey(
        Person,
        verbose_name="病人信息",
        related_name="diagnose_set",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        super(Diagnose, self).save(*args, **kwargs)
        img_path = os.path.abspath('.') + self.content.url
        self.status = effb6_apply(img_path)
        self.semantic = (unet_semantic(img_path)).split(os.path.abspath('.')+'/media/')[1]

        super(Diagnose,self).save(force_update=True)

    def admin_image(self):
        return '<img src="%s"/>' % self.content

    admin_image.allow_tags = True
