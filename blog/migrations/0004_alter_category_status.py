# Generated by Django 4.1.5 on 2023-01-30 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=True, verbose_name='ایا نمایش داده شود ؟'),
        ),
    ]