# Generated by Django 3.2.8 on 2021-11-16 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0005_review_user_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=200),
            preserve_default=False,
        ),
    ]
