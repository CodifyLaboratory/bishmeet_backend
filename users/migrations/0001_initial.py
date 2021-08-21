# Generated by Django 3.2.6 on 2021-08-20 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('age', models.CharField(max_length=20, verbose_name='Возраст')),
                ('gender', models.CharField(choices=[('others', 'Другое'), ('male', 'Мужской'), ('female', 'Женский')], max_length=20, verbose_name='Пол')),
                ('avatar', models.ImageField(upload_to='user_pictures/', verbose_name='Фото')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='Почта')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Дата/время регистрации')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='Последний вход')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]