# Generated by Django 4.2.6 on 2024-01-10 01:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sspanel", "0019_rename_ss_password_user_proxy_password_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="TicketMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.TextField(verbose_name="内容主体")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="时间"),
                ),
                (
                    "ticket",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="messages",
                        to="sspanel.ticket",
                        verbose_name="工单",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="用户",
                    ),
                ),
            ],
            options={
                "verbose_name": "工单回复",
                "verbose_name_plural": "工单回复",
                "ordering": ("ticket", "-created_at"),
                "indexes": [
                    models.Index(fields=["ticket", "created_at"], name="idx_ticket_created_at")
                ]
            },
        ),
    ]
