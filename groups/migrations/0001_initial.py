# Generated by Django 3.2.6 on 2021-08-20 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('interests', models.CharField(max_length=255, verbose_name='Интересы')),
                ('pictures', models.ImageField(null=True, upload_to='group_pictures/', verbose_name='Картинки')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.SmallIntegerField(verbose_name='Количество звезд')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_ratings', to='groups.group')),
            ],
            options={
                'verbose_name': 'Статистика группы',
                'verbose_name_plural': 'Статистики групп',
            },
        ),
    ]
