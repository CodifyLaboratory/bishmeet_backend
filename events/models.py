from django.db import models
from groups.models import Group
from users.models import User

answer_choices = (
    ('1', 'Интересно'),
    ('2', 'Пойду'),
    ('3', 'Не пойду')
)


class Event(models.Model):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL,
                              related_name='events', verbose_name='Группы', null=True)
    name = models.CharField(verbose_name='Название', max_length=255)
    location = models.CharField(verbose_name='Локация', max_length=255)
    description = models.TextField(verbose_name='Описание')
    event_date = models.DateField(verbose_name='Дата', auto_now=False)
    event_time = models.TimeField(verbose_name='Время', auto_now=False, null=True)
    pictures = models.ImageField(upload_to='event_pictures/', null=True, verbose_name="Картинки")
    active = models.CharField(verbose_name='Ваш ответ', max_length=20, choices=answer_choices, default=True)

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.name


class Rating(models.Model):
    start = models.SmallIntegerField(verbose_name='Количество звезд')
    event = models.ForeignKey(Event,
                              on_delete=models.CASCADE,
                              related_name='event_ratings')
    user = models.ForeignKey(to=User,
                             on_delete=models.SET_NULL,
                             related_name='users_ratings',
                             null=True)

    class Meta:
        verbose_name = 'Рейтинг мероприятия'
        verbose_name_plural = 'Рейтинги мероприятий'

    def __str__(self):
        return f'Мероприятие: {self.event.name}, рейтинг: {self.start}'


class Comment(models.Model):
    text = models.TextField(verbose_name='Текст')
    event = models.ForeignKey(to=Event,
                              on_delete=models.CASCADE,
                              related_name='events_comments')
    user = models.ForeignKey(to=User,
                             on_delete=models.SET_NULL,
                             related_name='users_comments',
                             null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.text[:100]}...'
