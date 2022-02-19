# Generated by Django 3.2.5 on 2021-10-12 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clginfoblog', '0005_rename_filters_filter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Filter',
        ),
    ]
