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
    birth = models.DateField(verbose_name="出生日期",default=timezone.now())
    sex = models.CharField(verbose_name= "性别",max_length=10, choices=GENDER_IN_CHOICES, default=UNKNOWN)
    Image = models.ForeignKey('CancerImage',verbose_name="检测结果", on_delete=models.CASCADE, null = True)
    updated = models.DateTimeField(verbose_name="最近检测时间", auto_now=True, null=True)

    class Meta:
        ordering = ('-updated',)


class CancerImage(models.Model):
    content = models.ImageField(upload_to='images/%Y%m%d')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, blank=True)
    semantic = models.ImageField(max_length=255, blank=True)

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        super(CancerImage, self).save(*args, **kwargs)
        self.status = effb6_apply(os.path.abspath('.') + self.content.url)
        self.semantic.save = ((unet_semantic(os.path.abspath('.') + self.content.url)).split(os.path.abspath('.')))[1]

        super(CancerImage, self).save(*args, **kwargs)

    def admin_image(self):
        return '<img src="%s"/>' % self.content

    admin_image.allow_tags = True
