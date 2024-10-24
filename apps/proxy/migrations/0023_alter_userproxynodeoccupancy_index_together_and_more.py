# Generated by Django 4.2.6 on 2023-12-22 01:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("proxy", "0022_proxynode_cost_price_relaynode_cost_price_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userproxynodeoccupancy",
            name="total_traffic",
            field=models.BigIntegerField(
                default=1073741824, verbose_name="总流量(单位字节)"
            ),
        ),
        migrations.AddField(
            model_name="userproxynodeoccupancy",
            name="used_traffic",
            field=models.BigIntegerField(default=0, verbose_name="已用流量(单位字节)"),
        ),
        migrations.AlterField(
            model_name="occupancyconfig",
            name="occupancy_price",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="价格"
            ),
        ),
        migrations.AlterField(
            model_name="occupancyconfig",
            name="occupancy_traffic",
            field=models.BigIntegerField(default=0, verbose_name="流量(单位字节)"),
        ),
        migrations.AlterField(
            model_name="occupancyconfig",
            name="occupancy_user_limit",
            field=models.PositiveIntegerField(default=0, verbose_name="用户数"),
        ),
        migrations.AlterField(
            model_name="occupancyconfig",
            name="proxy_node",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="occupancy_config",
                to="proxy.proxynode",
                verbose_name="代理节点",
            ),
        ),
        migrations.AlterField(
            model_name="proxynode",
            name="cost_price",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=10, verbose_name="成本"
            ),
        ),
        migrations.AlterField(
            model_name="proxynode",
            name="total_traffic",
            field=models.BigIntegerField(
                default=1073741824, verbose_name="总流量(单位字节)"
            ),
        ),
        migrations.AlterField(
            model_name="proxynode",
            name="used_traffic",
            field=models.BigIntegerField(default=0, verbose_name="已用流量(单位字节)"),
        ),
        migrations.AlterField(
            model_name="relaynode",
            name="cost_price",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=10, verbose_name="成本"
            ),
        ),
        migrations.AddIndex(
            model_name="userproxynodeoccupancy",
            index=models.Index(
                fields=["end_time"], name="proxy_userp_end_tim_ba27c4_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="userproxynodeoccupancy",
            index=models.Index(
                fields=["user", "end_time"], name="proxy_userp_user_id_a195e2_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="userproxynodeoccupancy",
            index=models.Index(
                fields=["proxy_node", "end_time"], name="proxy_userp_proxy_n_ffb646_idx"
            ),
        ),
        migrations.RemoveField(
            model_name="userproxynodeoccupancy",
            name="occupancy_config_snapshot",
        ),
        migrations.RemoveField(
            model_name="userproxynodeoccupancy",
            name="out_of_traffic",
        ),
        migrations.RemoveField(
            model_name="userproxynodeoccupancy",
            name="traffic_used",
        ),
    ]
