# Generated by Django 4.2.5 on 2023-10-15 00:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='topic',
            new_name='commentd_to',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='created_by_id',
            new_name='commented_by',
        ),
        migrations.RemoveField(
            model_name='topics',
            name='creted_by_id',
        ),
        migrations.AddField(
            model_name='topics',
            name='creted_by',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='topics_account', to=settings.AUTH_USER_MODEL, verbose_name='投稿者'),
        ),
    ]