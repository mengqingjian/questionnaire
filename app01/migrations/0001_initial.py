# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('val', models.IntegerField(blank=True, null=True)),
                ('content', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='班级名')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='选项名称')),
                ('score', models.IntegerField(verbose_name='选项对象的分值')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32)),
                ('type', models.IntegerField(choices=[('1', '打分'), ('2', '单选'), ('3', '评价')])),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='问卷名')),
                ('cls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.ClassRoom', verbose_name='班级中的所有问卷')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('cls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.ClassRoom', verbose_name='学生所在的班级')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uaername', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.UserInfo', verbose_name='班级创建者'),
        ),
        migrations.AddField(
            model_name='option',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Question', verbose_name='问题表中所有的单选'),
        ),
        migrations.AddField(
            model_name='answer',
            name='option',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.Option'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Question', verbose_name='所有回答的问题'),
        ),
        migrations.AddField(
            model_name='answer',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Student', verbose_name='所有学生回答的问题'),
        ),
    ]
