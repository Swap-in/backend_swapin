# Generated by Django 3.1 on 2020-08-22 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='clothes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on wich object was created.', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on wich object was last modified.', verbose_name='modified at')),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], max_length=8)),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=500)),
                ('size', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('FEMALE', 'FEMALE'), ('MALE', 'MALE'), ('OTHER', 'OTHER')], max_length=8)),
                ('picture_1', models.CharField(max_length=500)),
                ('picture_2', models.CharField(blank=True, max_length=500, null=True)),
                ('picture_3', models.CharField(blank=True, max_length=500, null=True)),
                ('picture_4', models.CharField(blank=True, max_length=500, null=True)),
                ('picture_5', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_like', models.CharField(choices=[('LIKE', 'LIKE'), ('SUPERLIKE', 'SUPERLIKE'), ('DISLIKE', 'DISLIKE')], max_length=15)),
                ('clothe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.clothes')),
            ],
        ),
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on wich object was created.', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on wich object was last modified.', verbose_name='modified at')),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], max_length=8)),
                ('date', models.DateTimeField()),
                ('read', models.BooleanField(default=False)),
                ('send', models.BooleanField(default=False)),
                ('like_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.like')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
