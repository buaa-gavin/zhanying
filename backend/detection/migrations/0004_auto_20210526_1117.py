# Generated by Django 3.2.3 on 2021-05-26 03:17

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0003_alter_person_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ImageField(upload_to='images/%Y%m%d')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(blank=True, max_length=255)),
                ('semantic', models.ImageField(blank=True, max_length=255, upload_to='')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ('-updated',)},
        ),
        migrations.RemoveField(
            model_name='person',
            name='Image',
        ),
        migrations.AddField(
            model_name='person',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='最近检测时间'),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth',
            field=models.DateField(default=datetime.datetime(2021, 5, 26, 3, 17, 53, 854217, tzinfo=utc), verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(choices=[('unknown', '未知性别'), ('m', '男'), ('f', '女')], default='unknown', max_length=10, verbose_name='性别'),
        ),
        migrations.DeleteModel(
            name='CancerImage',
        ),
        migrations.AddField(
            model_name='diagnose',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='diagnose_set', to='detection.person', verbose_name='病人信息'),
        ),
    ]
