# Generated by Django 5.1 on 2024-10-24 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proxy', '0031_ssconfig_remark_strongswanconfig_remark_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ssconfig',
            name='remark',
        ),
        migrations.RemoveField(
            model_name='strongswanconfig',
            name='remark',
        ),
        migrations.RemoveField(
            model_name='trojanconfig',
            name='remark',
        ),
    ]
