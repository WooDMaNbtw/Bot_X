# Generated by Django 4.2.7 on 2023-12-13 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('proxy_method', models.CharField(blank=True, max_length=10, null=True)),
                ('proxy_url', models.URLField(blank=True, max_length=255, null=True)),
                ('proxy_request_headers', models.JSONField(blank=True, null=True)),
                ('proxy_request_body', models.JSONField(blank=True, null=True)),
                ('proxy_response_headers', models.JSONField(blank=True, null=True)),
                ('proxy_response_body', models.JSONField(blank=True, null=True)),
                ('proxy_response_status_code', models.PositiveIntegerField(blank=True, null=True)),
                ('core_method', models.CharField(blank=True, max_length=10, null=True)),
                ('core_url', models.URLField(blank=True, max_length=255, null=True)),
                ('core_request_headers', models.JSONField(blank=True, null=True)),
                ('core_request_body', models.JSONField(blank=True, null=True)),
                ('core_response_headers', models.JSONField(blank=True, null=True)),
                ('core_response_body', models.JSONField(blank=True, null=True)),
                ('core_response_status_code', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
                'ordering': ['id'],
            },
        ),
    ]
