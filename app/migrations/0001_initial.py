# Generated by Django 2.2.25 on 2022-01-30 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='タイトル')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='画像')),
                ('content', models.TextField(verbose_name='本文')),
                ('updata_at', models.DateField(default=django.utils.timezone.now, verbose_name='更新日')),
                ('create_at', models.DateField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
