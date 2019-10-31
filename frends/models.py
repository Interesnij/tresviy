from django.db import models
from django.conf import settings
from notifications.models import Notification, notification_handler
from django.contrib.auth.models import User


class Connect(models.Model):
    user = models.ForeignKey(User, db_index=False, on_delete=models.CASCADE, related_name='connections', verbose_name="Инициатор перевода из подписчика в друзья")
    target_user = models.ForeignKey(User, db_index=False, on_delete=models.CASCADE, related_name='targeted_connections', null=False, verbose_name="Кого переводит из подписчика в друзья")
    target_connection = models.OneToOneField('self', on_delete=models.CASCADE, null=True)

    def notification_connect(self, user):
        notification_handler(user, self.target_user, Notification.CONNECTION_CONFIRMED, action_object=self, id_value=str(user.uuid), key='notification')

    @classmethod
    def create_connection(cls, user_id, target_user_id):
        target_connection = cls.objects.create(user_id=user_id, target_user_id=target_user_id)
        target_connection.notification_follow(user_id)
        target_connection.save()
        return target_connection

    class Meta:
        unique_together = ('user', 'target_user')
        verbose_name = 'Друг'
        verbose_name_plural = 'Друзья'
