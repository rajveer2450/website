# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-10 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0065_finalapplication_community_specific_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalapplication',
            name='community_specific_questions',
            field=models.TextField(blank=True, help_text='Some communities or projects may want you to answer additional questions. Please check with your mentor and community coordinator to see if you need to provide any additional information after you save your project application.', max_length=8000, verbose_name='(Optional) Community-specific Questions'),
        ),
    ]
