import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.utils import timezone
from django.contrib.postgres.indexes import BrinIndex
from django.db import transaction
from notifications.models import Notification, notification_handler
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models import Q


class Item(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True,verbose_name="uuid")
    comments_enabled = models.BooleanField(default=True, verbose_name="Разрешить комментарии")
    #community = models.ForeignKey('communities.Community', db_index=False, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Сообщество")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=False, on_delete=models.CASCADE, verbose_name="Создатель")
    is_edited = models.BooleanField(default=False, verbose_name="Изменено")
    is_closed = models.BooleanField(default=False, verbose_name="Закрыто")
    is_deleted = models.BooleanField(default=False, verbose_name="Удалено")
    is_fixed = models.BooleanField(default=False, verbose_name="Закреплено")
    is_repost = models.BooleanField(verbose_name="Это репост", default=False)
    views=models.IntegerField(default=0, verbose_name="Просмотры")
    moderated_object = GenericRelation('moderation.ModeratedObject', related_query_name='items')
    parent = models.ForeignKey("self", blank=True,
        null=True, on_delete=models.CASCADE, related_name="thread")

    class Meta:
        indexes = (
            BrinIndex(fields=['created']),
        )

        ordering = ['-id']

    def save(self, *args, **kwargs):
        if not self.is_fixed:
            return super(Item, self).save(*args, **kwargs)
        with transaction.atomic():
            Item.objects.filter(
                is_fixed=True).update(is_fixed=False)
            return super(Item, self).save(*args, **kwargs)

    def count_comments(self):
        parent_comments = ItemComment.objects.filter(item=self).count()
        return parent_comments

    def get_replies(self):
        get_comments = ItemComment.objects.filter(parent_comment=self).all()
        return get_comments

    def notification_like(self, user):
        notification_handler(user, self.creator,Notification.LIKED, action_object=self,id_value=str(self.uuid),key='social_update')

    def notification_dislike(self, user):
        notification_handler(user, self.creator,Notification.DISLIKED, action_object=self,id_value=str(self.uuid),key='social_update')

    def notification_comment(self, user):
        notification_handler(user, self.creator,Notification.POST_COMMENT, action_object=self,id_value=str(self.uuid),key='notification')

    def get_parent(self):
        if self.parent:
            return self.parent
        else:
            return self

    def get_thread(self):
        parent = self.get_parent()
        return parent.thread.all()

    def count_thread(self):
        return self.get_thread().count()

    def __str__(self):
        return "{0}/{1}".format(self.creator.get_full_name(), self.views)


class ItemComment(models.Model):
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,verbose_name="Родительский комментарий")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    modified = models.DateTimeField(auto_now_add=True, auto_now=False, db_index=False)
    commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Комментатор")
    text = models.TextField(blank=True,null=True)
    is_edited = models.BooleanField(default=False, null=False, blank=False,verbose_name="Изменено")
    is_deleted = models.BooleanField(default=False,verbose_name="Удаено")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)

    class Meta:
        indexes = (
            BrinIndex(fields=['created']),
        )

    def __str__(self):
        return "{0}/{1}".format(self.commenter.get_full_name(), self.text[:10])


class EmojiGroup(models.Model):
    keyword = models.CharField(max_length=32, blank=False, null=False)
    order = models.IntegerField(unique=False, default=100)
    created = models.DateTimeField(editable=False)
    is_reaction_group = models.BooleanField(default=False)

    def __str__(self):
        return 'EmojiGroup: ' + self.keyword

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super(EmojiGroup, self).save(*args, **kwargs)


class Emoji(models.Model):
    group = models.ForeignKey(EmojiGroup, on_delete=models.CASCADE, related_name='emojis', null=True)
    keyword = models.CharField(max_length=16, blank=False, null=False)
    image = models.ImageField(blank=False, null=False, upload_to="emoji/")
    created = models.DateTimeField(editable=False)
    order = models.IntegerField(unique=False, default=100)

    def __str__(self):
        return 'Emoji: ' + self.keyword

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        return super(Emoji, self).save(*args, **kwargs)


class ItemReaction(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    created = models.DateTimeField(editable=False)
    reactor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    emoji = models.ForeignKey(Emoji, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('reactor', 'item', 'emoji')

    def __str__(self):
        return "{0}/{1}".format(self.item.creator.get_full_name(), self.emoji.keyword)

    def count_emoji(self):
        count_emoji = Emoji.objects.filter(itemreaction=self).count()
        return count_emoji

    def get_emoji(self):
        emojis = Emoji.objects.filter(itemreaction=self).all()
        return emojis


class ItemCommentReaction(models.Model):
    item_comment = models.ForeignKey(ItemComment, on_delete=models.CASCADE, related_name='reactions')
    created = models.DateTimeField(editable=False)
    reactor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_comment_reactions')
    emoji = models.ForeignKey(Emoji, on_delete=models.CASCADE, related_name='post_comment_reactions')

    class Meta:
        unique_together = ('reactor', 'item_comment',)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super(ItemCommentReaction, self).save(*args, **kwargs)


class ProxyBlacklistedDomain(models.Model):
    domain = models.CharField(max_length=100, unique=True)

    @classmethod
    def is_url_domain_blacklisted(cls, url):
        url = url.lower()
        if not urlparse(url).scheme:
            url = 'http://' + url
        tld_extract_result = tldextract.extract(url)
        url_root_domain = '.'.join([tld_extract_result.domain, tld_extract_result.suffix])
        url_full_domain = '.'.join([tld_extract_result.subdomain, tld_extract_result.domain, tld_extract_result.suffix])
        return cls.objects.filter(Q(domain=url_root_domain) | Q(domain=url_full_domain)).exists()
