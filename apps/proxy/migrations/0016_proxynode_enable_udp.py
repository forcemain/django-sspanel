# Generated by Django 4.1.3 on 2023-02-01 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("proxy", "0015_alter_proxynode_server_alter_relaynode_server_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="proxynode",
            name="enable_udp",
            field=models.BooleanField(default=True, verbose_name="是否开启UDP 转发"),
        ),
    ]
