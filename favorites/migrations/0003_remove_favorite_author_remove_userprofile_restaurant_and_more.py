# Generated by Django 4.1 on 2024-09-24 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('details', '0006_remove_restaurant_is_favorite_and_more'),
        ('favorites', '0002_remove_favorite_post_id_favorite_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='author',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='favorite',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='details.restaurant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
