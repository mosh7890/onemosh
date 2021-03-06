# Generated by Django 2.2 on 2019-04-04 11:28

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0002_auto_20190403_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=stdimage.models.StdImageField(blank=True, help_text='Picture:JPG/JPEG.', null=True,
                                                upload_to='users/profile_pics', verbose_name='Profile Picture'),
        ),
    ]
